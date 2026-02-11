#############################
class Student:
  def __init__(self):
    pass

  def __call__(self):     ## To make instance of the class callable, It should have __call__ special function
    pass  


callable(Student)       ##Class is always callable
student1=Student()    
callable(student1)

######################################
from abc import ABC,abstractmethod
class Payment(ABC):
  @abstractmethod
  def pay():
    pass

class CreditCard(Payment):
  def __init__(self,amount):
    self.amount=amount

  def pay(self):
    return f'Amount paid {self.amount}'  
  
  
  def amounToPay(self):
    return f'Paying {self.amount}'

cc1=CreditCard(3000)
#cc1.amounToPay()
cc1.pay()
