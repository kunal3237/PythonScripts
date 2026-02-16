# This example shows Enacapsulation/Polymorphism/Abstraction
from abc import ABC,abstractmethod

class Payment(ABC):
  def __init__(self,):
    print(f'This is the abstraction class')
  
  @abstractmethod
  def pay(self,amount):
    pass  

class CreditCard(Payment):
  def __init__(self):
    print('Payment from Credit Card')

  def pay(self,amount):
    self.__amount=+amount
    return f'{self.__amount}'

  @property
  def amount(self):
    return f'{self.__amount}'  

  @amount.setter
  def amount(self,admin_amount) : 
    self.__amount=+admin_amount
    return f'{self.__amount}'

class Upi(Payment):
  def __init__(self):
    self.__amount=0
    print('Payment from UPI')

  def pay(self,amount):
    self.__amount=+amount
    return f'{self.__amount}'       ### Varaible inside is being called even it is private. However we can access it from external
    

#payment1=Payment()    ## You can't intiate tht Abstract class

cc1=CreditCard()
cc1.pay(1000)
upi1=Upi()
upi1.pay(300)
#print(upi1.__amount)
#print(upi1._Upi__amount)     # This is how we can access it externally. To show name only. However better to use getter
print(cc1.amount)
cc1.amount=500
print(cc1.amount)
