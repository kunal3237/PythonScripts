### Everything in python is Object. OOPs is related to real life examples. Pythin provides internal data type, But we can create new data type for ourself
## based on our requirement.  I am creating two class for my work. Here DOg and owner are 2 classes(data types for my use case)

This example 
class Dog:
  def __init__(self,name,breed,owner=None):      #### Setting owner=None as I want to use the owner object later on. Else it will complain
    self.name=name
    self.breed=breed
    self.owner=owner
  def bark(self):
    return f'{self.owner.name}s dog Woofing Woofing'      ### Calling owner object attribute
  

class Owner:
 def __init__(self,name,address,phno,dog):        ###Passing dog object here
  self.name=name
  self.address=address
  self.phno=phno        ## Here created two classes and using the object of the one object in other object
  self.dog=dog

  
 def command(self):
  return f' Command Passed by {self.name} to {self.dog.name}'

dog1=Dog('oscar','lab')  
dog2=Dog('jimmy','local')
owner1=Owner('kunal','Palam',2321,dog1)
dog1.owner=owner1    ### As intial owner wa set to NOne. once dog object is created now I wan to pass it the owner object
owner2=Owner('Manu','Palam',5353,dog2)
dog2.owner=owner2

### with Dog class I can get the owner details as owner is object here

owner1.command()
dog1.bark()
dog2.bark()
          
