"""
Expected Output Snippet
__________________________________
#######This script will give you the Public IP of the service for requested region######
please enter the region name ....: ap-south-2
IP : 98.131.0.0/16
Region of the service: ap-south-2
Service Name: AMAZON
------------------------------------------------------------------------------------------
IP : 52.93.115.0/24
Region of the service: ap-south-2
Service Name: AMAZON
------------------------------------------------------------------------------------------
IP : 15.177.94.0/24
Region of the service: ap-south-2
Service Name: AMAZON
------------------------------------------------------------------------------------------
"""

#Author : Kunal Sharma
#Print the IP of the aws Public services

import requests

response=requests.get('https://ip-ranges.amazonaws.com/ip-ranges.json')

print()
print('#######This script will give you the Public IP of the service for requested region######')
region_ask=input("please enter the region name ....: " )
region_ask="".join(region_ask.split())      #Converting List to string

def public_service_detail():
   
        response_data_out=response.json()
        region_list=[]
        for j in response_data_out["prefixes"]:
              region_list.append(j["region"])
            
        if region_ask not in region_list:
            print('No Such Region, Please check the region name....')
        else:    
            
            for i in response_data_out["prefixes"]:
                if i['region']==region_ask:
                    print(f"IP : {i['ip_prefix']}")
                    print(f"Region of the service: {i['region']}")
                    print(f"Service Name: {i['service']}")
                    print("---"*30)
                else:
                    pass    
                
def main():
    public_service_detail()
    
main()    
