"""
Expected OutPut of the vpc-creation.py script


**************************************************
New VPC Created with VpcId: vpc-02************8
Subnet created with SubnetId: subnet-03*************
Subnet created with SubnetId: subnet-01************
Subnet created with SubnetId: subnet-0f************
**************************************************
CIDR of the Vpc Created: 10.100.0.0/16
State of the VPC is : associated
Default VPC : False
--------------------------------------------------
Subnet No: 1
Subnet Id of the subnet is : subnet-03************
Subnet ARN of the subnet is : arn:aws:ec2:ap-south-1:**************:subnet/subnet-03************
Subnet ARN of the subnet is : 10.100.1.0/24
--------------------------------------------------
Subnet No: 2
Subnet Id of the subnet is : subnet-0f************
Subnet ARN of the subnet is : arn:aws:ec2:ap-south-1:************:subnet/subnet-0f6************
Subnet ARN of the subnet is : 10.100.3.0/24
--------------------------------------------------
Subnet No: 3
Subnet Id of the subnet is : subnet-01************
Subnet ARN of the subnet is : arn:aws:ec2:ap-south-1:************:subnet/subnet-01************
Subnet ARN of the subnet is : 10.100.2.0/24
--------------------------------------------------
**************************************************
Do you want to see the list of all existing vpc....y
**************************************************
Vpc Number: 1
CIDR of the Vpc: 172.31.0.0/16
State of the VPC is : associated
VpcId of the VPC : vpc-6e************
Default VPC : True
**************************************************
Vpc Number: 2
CIDR of the Vpc: 10.100.0.0/16
State of the VPC is : associated
VpcId of the VPC : vpc-02************
Default VPC : False
**************************************************
""""

import boto3

   
ec2_client=boto3.client('ec2')   

response_vpc_creation=ec2_client.create_vpc(
    CidrBlock='10.100.0.0/16',
    AmazonProvidedIpv6CidrBlock=True,
    InstanceTenancy='default',
    
)
print('*'*50)
new_created_vpc=response_vpc_creation['Vpc']['VpcId']
print(f"New VPC Created with VpcId: {new_created_vpc}")

for i in ['10.100.1.0/24','10.100.2.0/24','10.100.3.0/24']:
    subnet_create=ec2_client.create_subnet(
       CidrBlock=i,
       VpcId=new_created_vpc,
        )
    print(f"Subnet created with SubnetId: {subnet_create['Subnet']['SubnetId']}")

response_vpc = ec2_client.describe_vpcs(
    Filters=[
        {
          
            'Name': 'vpc-id',
            'Values': [new_created_vpc,
            ]
        },
    ],
        
)
print('*'*50)
for i in response_vpc['Vpcs']:
    for j in i['CidrBlockAssociationSet']:
        print(f"CIDR of the Vpc Created: {j['CidrBlock']}")
        print(f"State of the VPC is : {j['CidrBlockState']['State']}")
        print(f"Default VPC : {i['IsDefault']}")

response_subnet = ec2_client.describe_subnets(
    Filters=[
        {
            'Name': 'vpc-id',
            'Values': [new_created_vpc
                ,
            ]
        },
    ],
    )

print('-'*50)
subnet_count=0
for i in response_subnet['Subnets']:
    subnet_count+=1
    print(f"Subnet No: {subnet_count}")
    print(f"Subnet Id of the subnet is : {i['SubnetId']}")
    print(f"Subnet ARN of the subnet is : {i['SubnetArn']}")
    print(f"Subnet ARN of the subnet is : {i['CidrBlock']}")
    print('-'*50)
    
    
print('*'*50)

while True:
    input_capture=input("Do you want to see the list of all existing vpc....")
    if input_capture.isalpha() and input_capture.lower()=='y' or input_capture.isalpha() and input_capture.lower()=='yes':
     
        response_vpc = ec2_client.describe_vpcs(
                    
            )
        print('*'*50)
        vpc_count=0
        for i in response_vpc['Vpcs']:
            vpc_count+=1
            for j in i['CidrBlockAssociationSet']:
                    
                    print(f"Vpc Number: {vpc_count}")
                    print(f"CIDR of the Vpc: {j['CidrBlock']}")
                    print(f"State of the VPC is : {j['CidrBlockState']['State']}")
            print(f"VpcId of the VPC : {i['VpcId']}")
            print(f"Default VPC : {i['IsDefault']}")
            print('*'*50)
        break
    else:
        print('Thank you, Bye!!!')
        break
