#####################################################
### Encapsulation example (with Protected _ and Private attributes __ ). Here er are controlling the acces of the attributes
class Seller:
  def __init__(self,name,address,gstin,tax):      ###Constructor
    self.name=name
    self.address=address
    self._gstin=gstin         ###Protected
    self.__tax=tax            ####Private

  @property                   # Created a getter method to contorl the access of the attribute,even though it protected can be changed
  def gstin(self):        #externally. 
    return f'{self._gstin}'

  @property                 ###Getter method for Private Attribute. This is Private, it can be changed and access externally
  def tax(self):        
    return f'{self.__tax}'  #### Name mangled to seller1._Seller__tax i.e obj._Class__attribute

  @tax.setter         ### Name should match with getter name,even the name of the function being used in the getter and setter
  def tax(self,new_tax):
      self.__tax=new_tax
      return f'{self.__tax}'    ### This is for testing. 

  def sell(self):
    return f'I am selling'

  def add_inventory(self):
    return f'Added in the inventory'

  def check_inventory(self):
    return f'Checking in the inventory'    


seller1=Seller('kunal','Palampur',244,5453)
print(seller1._gstin) 
seller1._gstin=455 
print(seller1._gstin)    ### Attribute is protected ,even then it can be modified from outside
print(seller1.gstin)
#print(seller1.__tax)    ### This will complain as it's name is mangled, can't be access 
#print(seller1._Seller__tax)
#seller1.__tax=4343
#print(seller1.__tax)    ### It is changed because now it is new attribute
#print(dir(seller1))
print(seller1.tax)
seller1.tax=4355354     ## once you configure getter and setter. Make sure you use those as attribute not as a function
print(seller1.tax)

#########################################################################

#### Inhertance Example i.e Direct Inheritance, Inheritance works on "is" relationship. Inheritance represents an IS-A relationship 
#where the child reuses and extends parent behavior.

class Person:
  def __init__(self,name,address):
    self.name=name
    self.address=address

  def talk(self):
    return f'{self.name} talk'

  def walk(self):
    return f'{self.name} walk to {self.address}'

class Login:
  def __init__(self,username,pasword):
    self.username=username
    self.pasword=pasword

  def show_profile(self):
    return f'{self.username} Logged in .. '

  def add_post(self,post):
      return f'I am travelling to {post}.. Hurray'

class User(Person):                                   ### User inherit the Person class "User is a Person"
  def __init__(self, name, address,insta_account):
    super().__init__(name, address)
    self.insta_account=insta_account

  def send_friend_request(self,other):
    return f'I {self.name} am sending request to {other} '

  def account_check(self,login):           #### Login object used here as composition "User has login", Better to pass it with constructor
    self.login=login
    return f' I am logged in and showing my profile {login.show_profile()}'  

login1=Login('kunal','9790')
user1=User('kunal','Palam','1234')   
print(user1.walk())
user1.send_friend_request('sharma')
user1.account_check(login1)


##############################################################
#####################
####Polyphormism Example. Polyphormism means multilple forms. Heer I 'll show you the same methods with different working
from abc import ABC,abstractmethod
class Payment(ABC):
  # def __init__(self):
  #   # self.name=name
  #   # self.qty=qty
  
  @abstractmethod
  def pay(self):
    pass

  def buy(self):
    pass


class creditCard_payment(Payment):
  def __init__(self):
    #super().__init__(name,qty)
    print (f'This is from Credit card')

  def pay(self):
    return f'Paying it from Credit Card'

class upi_payment(Payment):
  def __init__(self):
    #super().__init__(name,qty)
    print(f'This is from Upi')           

  def pay(self):
    return f'Paying it from Upi'
    
  
# up1=upi_payment() 
# cc1=creditCard_payment()
# up1.pay()
# cc1.pay()
payment=[upi_payment(),creditCard_payment()]
for i in payment:
  i.pay()


