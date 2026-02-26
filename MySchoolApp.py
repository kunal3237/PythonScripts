import json
class SchoolApp:
  SCHOOLNAME='Primary School'
  def __init__(self):
   print(f'{SchoolApp.SCHOOLNAME}')

  def registerStudent(self,**kwargs):
    mydict={}
    for key,value in kwargs.items():
      mydict[key]=value
      with open('studentrecord.txt','a') as w:
       json.dump(mydict,fp=w)      #### serializes Python dict to JSON and writes to file
       w.write('\n')

 
  def checkStudent(self,name):
      
      with open('studentrecord.txt','r') as o:
        for line in o:
          check=json.loads(line)        # json.dumps is used to create a python object
          if check.get("name") ==name:
            print(f'{name}')
            return

      print(f'{name} not found')      
      return False




        


school=SchoolApp()
school.registerStudent(name='kunal')  
school1=SchoolApp()
school1.registerStudent(name='sharma') 

school3=SchoolApp()
school3.registerStudent(name='kunal') 
school.checkStudent('kunal') 

      
