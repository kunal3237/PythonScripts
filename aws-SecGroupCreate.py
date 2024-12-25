import boto3
import random


"""This script is to create new Security
Group with ingress defined with in the Security rules"""


try: 
    grouprand=str(random.randint(1,99999))
    group_name='SG-Ingress-Python' + grouprand
    security_group=boto3.client('ec2')
    response_sg=security_group.create_security_group(
        Description='Secrity Group creted with Python script',
        GroupName=group_name,
        
    )
    print(f"Security Group Created : {response_sg['GroupId']}")
    def sg_association_func(ip_cidr='0.0.0.0/0',fromport=80,toport=80):
        response_sg_rules=security_group.authorize_security_group_ingress(
            GroupId=response_sg['GroupId'],
            IpPermissions=[
                {
                    'IpProtocol': 'tcp',
                    'FromPort': fromport,
                    'ToPort': toport,
                    'IpRanges': [
                        {
                            'Description': 'IP range with python script',
                            'CidrIp': ip_cidr
                        },
                    ],
                },
            
                ],
        
            )
        return response_sg_rules


    sg_association=input('Do you want to Define the rules for Security Group: ')
    while True:
            
            if sg_association.isalpha() and sg_association.lower()=='y' or sg_association.isalpha() and sg_association.lower()=='yes':
                print("Please enter the CIDR, FromPort and ToPort")
                ip_cidr=input("CIDR, Please ( eg. 192.168.0.0/32): ")
                fromport=int(input("FromPort, Please : "))
                toport=int(input("ToPort, Please : "))
                response_sg_rules=sg_association_func(ip_cidr,fromport,toport)
                print("*"*50)    
                print(f"Security Group Created : {response_sg['GroupId']}")
                
                for i in response_sg_rules['SecurityGroupRules']:
                    print(f"Is this egress Rule: {i['IsEgress']}")   
                    print(f"IP4 Address Allowed: {i['CidrIpv4']}")
                    print(f"From Port Allowed: {i['FromPort']}")
                    print(f"To Port Allowed: {i['ToPort']}")
                mygroupid=response_sg['GroupId']    
                response_sg_rules_vpc=security_group.describe_security_groups(
                        GroupIds=[
                                    mygroupid,
                                                ],
                        Filters=[
                        {
                            'Name': 'group-id',
                            'Values': [
                                    mygroupid,
                                    ]
                                },
                                    ]
                            )   

                for i in response_sg_rules_vpc['SecurityGroups']:
                    print(f"VPC to which this SG is assocaiated : {i['VpcId']}")
        
                print("*"*50)        
                sg_association=input("Do you want to add more Rules: ...")
                if sg_association.isalpha() and sg_association.lower()=='y' or sg_association.isalpha() and sg_association.lower()=="yes":
                    continue
                else:
                    print("Thanks for using the script..")
                    break 
                    
            else:
                break 
            
                    
except Exception as error:
    print(error)            
                






                    
                    

    


