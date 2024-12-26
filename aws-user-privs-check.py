"""
Expected Report
_________________________________________________
--------------------------------------------------
List of users with attached direct policies
**************************************************
kunal: AdministratorAccess
oscar: No Direct Policy Attached
sharma: AdministratorAccess
--------------------------------------------------
User Group List
--------------------------------------------------
kunal: mygroup1
kunal: mygroup
oscar: Not a member of group
sharma: mygroup
--------------------------------------------------

mygroup1: Group Policices

AIOpsReadOnlyAccess
--------------------------------------------------

mygroup: Group Policices

IAMReadOnlyAccess
AmazonEC2ContainerRegistryReadOnly
--------------------------------------------------
**************************************************
"""

#To Check AWS user and their Privs and groups assigment
# Author : Kunal Sharma

import boto3
client_iam=boto3.client('iam')


response_iam_user=client_iam.list_users(
    )

def userlist_available():
    username_list=[]
    for i in response_iam_user['Users']:
        username_list.append(i['UserName'])
    return username_list



            
def userlist_policy_check():
        username_list=userlist_available()
        for i in username_list:
            response_iam_policies=client_iam.list_attached_user_policies(
                    UserName=i,
                                )

            if response_iam_policies['AttachedPolicies']==[]:
                print(f"{i}: No Direct Policy Attached")
            else:
                for j in response_iam_policies['AttachedPolicies']:
                    print(f"{i}: {j['PolicyName']}")   
 
def user_group_list():
    username_list=userlist_available()
    group_set=set({})
    for i in username_list:
            response_group_list=client_iam.list_groups_for_user(
            UserName=i,
                     )
            if response_group_list['Groups']==[]:
                print(f"{i}: Not a member of group")
            else:
                
                for j in response_group_list['Groups']:
                    print(f"{i}: {j['GroupName']}")
                    group_set.add(j['GroupName'])
                    
                    
    print('-'*50)
    
    for i in group_set:
        response_group_policies = client_iam.list_attached_group_policies(
                                     GroupName=i,
                                     )
        print()
        print(f"{i}: Group Policices")
        print()
        for k in response_group_policies['AttachedPolicies']:
                        
                        print(k['PolicyName'])    
        print('-'*50)                    
            #print(group_set)                
                    # group_name=j['GroupName']
                    # print("*"*50)
                    # print(f"Group : {group_name} Attached Policies")
                    # print("*"*50)
                    # response_group_policies = client_iam.list_attached_group_policies(
                    #                 GroupName=group_name,
                    #                 )
                    # for k in response_group_policies['AttachedPolicies']:
                    #     print(k['PolicyName'])
                        
                    #print(f"{j} : {response_group_policies['PolicyName']}")      

def main():
   userlist_policy_check()
   print('-'*50)
   print("User Group List")
   print('-'*50)
   user_group_list()
   
print('-'*50)
print('List of users with attached direct policies')
print("*"*50)   
main()    
print("*"*50)



