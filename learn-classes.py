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
          
########################################################

"""This example to use inhertance i.e Direct inheritance. employee and customer are 2 classes which have different role in
bank. But both entities use same login mechanism to lofgin into the portal"""

class Login:
  def __init__(self):
    print(f'Welcome in our site')
    
  def loggingIn(self,username,password):
    if password == 0000:
      print(f'Logged in ..... Welcome')
    else:
      print(f'Please check your credentials...')  

class Employee(Login):
  def __init__(self,name,position):
    self.name=name
    self.position=position

  def interestRate(self):
    if self.position <5:
      inr_rate=7
      print(f'Interest rate for this employee is {inr_rate} ')
    else:
      inr_rate=9
      print (f'Interest rate for this employee is {inr_rate}')  
  def houseing(self):
    if self.position < 5:
      print(f'This employee will get HRA of 40000')
    else:
      print(f'This employee will get HRA of 20000')

class Customer(Login):
  def __init__(self,name,contact):
    super().__init__()              #### When Both and parent have constructor then child use its constructor. 
    self.name=name                  ## However We can call the parent constructor or other entities using super() method
    self.contact=contact
    self.amount=0

  def deposit(self,amount):
    print(f'{self.name} deposited {amount}')  
    self.amount=self.amount+amount

  def display_amount(self):
    print(f'Current Amount in your account is {self.amount}')

employee1=Employee('kunal',3)

# employee1.loggingIn('kunal',0)
# employee2=Employee('rahul',7)
# employee1.interestRate()
# employee1.houseing()
# employee2.interestRate() 
# employee2.houseing()
customer1=Customer('oscar',344234)        
# customer1.deposit(50000)
# customer1.display_amount()  
customer1.loggingIn('sharma',0)


##############################################


"""__ is private to class and can't be accessed or changed directly from outside. To access/change it from outside
we user getter @property and setter. Methods can also be set private but there is not such getter and setter for methods.
So if you want to use the private method use it internally """
class Student:
  def __init__(self,name,rollno):
    ###self.name=name      This is problematic as this value can be changed extenrally. So better to encapsulate the attribute or method
    ### whic you want not to be changed externally
    self.__name=name    ## THis is name mangling so can't be directly changed
    self.rollno=rollno

  @property           ### Gettter created here
  def getName(self):
    print(f'My name is {self.__name}')  

  @getName.setter
  def getName(self,name):
    self.__name=name
      

  def __study(self):
    print(f'I am studying {self.__name}')

  def play(self):
    print(f'I am playing {self.__name}')

  def attendence(self):
    print(f'Rollno .. {self.rollno} present Mam and {self.__study()}')

student1=Student('kunal',8)

student1.getName      
student1.getName='sharma'
student1.getName
student1.attendence()
########################################################
"""Here we will dscuss protected attributes and methods, Protected attributes are mainly for subclasses and
message to programers that these are internal"""

class Student:
  def __init__(self,name,Rollno):
    self._name=name
    self.rollno=Rollno

  def study(self):
    return f'Hi My name is {self._name} and I am studying' 

student1=Student('kunal',9)
student1.study()
student1._name='sharma'
student1.study()

###############################################################

class User:
  def __init__(self,name,email):
    self.name=name
    self.email=email
    self.profile={}
  def createProfile(self,**kwargs):
    self.profile.update(kwargs)
   
   
    return 'Profile Created ... '

  def showProfile(self):
    return  self.profile  

user1=User('kunal','kunal@outlook.com')  
user1.createProfile(name='kunal',email='kunal@outlook.com',age=40)  
print(user1.showProfile())
user2=User('sharma','sharma@outlook.com')  
user2.createProfile(name='sharma',email='sharma@outlook.com',age=40)  
print(user2.showProfile())
print(user1.showProfile())
