#Author" Kunal Sharma
# Script to interact with Api and Json data
"""
Expected OutPut
_______________________________________
Date : 2024-12-27
TimeZone: America/New_York
First Light: 5:51:11 AM
Last Light: 6:30:04 PM
Day Length: 9:27:09
"""
"""
While working with api, you might come acroos json data, Json is a widely-used text-based format for data interchange. Its syntax 
resembles Python dictionaries but with some differences, such as using only double quotes for strings and lowercase for Boolean values. 
for example in below json data save in json_data variable, key "isDog" has value of "true".
to work with json data json module has load,loads,dump,dumps methods

Serialize & Deserialize
Example json data

json_data=\"""{
  "name": "Frieda",
  "isDog": true,
  "hobbies": ["eating", "sleeping", "barking"],
  "age": 8,
  "address": {
    "work": null,
    "home": ["Berlin", "Germany"]
  },
  "friends": [
    {
      "name": "Philipp",
      "hobbies": ["eating", "sleeping", "reading"]
    },
    {
      "name": "Mitch",
      "hobbies": ["running", "snacking"]
    }
  ]
}\"""
"""

import requests 
import json

class Weather_check():
    def __init__(self,url):
        self.url=url

    def weather_display(self):
        response_weather_api=requests.get(self.url)
        weather_data_weather=json.loads(response_weather_api.text)
        return (
        f"Date : {weather_data_weather['results']['date']}\n"
        f"TimeZone: {weather_data_weather['results']['timezone']}\n"
        f"First Light: {weather_data_weather['results']['first_light']}\n"
        f"Last Light: {weather_data_weather['results']['last_light']}\n"
        f"Day Length: {weather_data_weather['results']['day_length']}\n"      
        )
url="https://api.sunrisesunset.io/json?lat=38.907192&lng=-77.036873"        
check_weather=Weather_check(url) 
print(check_weather.weather_display())       
                
# #url="https://jsonplaceholder.typicode.com/posts/1/comments"






