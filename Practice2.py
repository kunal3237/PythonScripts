## This example will show Encapsulation,Getter,Setter and Composition
class User:
  def __init__(self,name,address,email):
    self.name=name
    self.email=email
    self.address=address


class Expense:
  def __init__(self,id,amount,description):
    self.id=id
    self.amount=amount
    self.desc=description


class UserService:
  def __init__(self,user):          ### Using Composition, Not Inheritance
    self.user=user

  def create_user(self):
    print( f'{self.user.name}.. User Created.. Calling ')

  def change_user(self,name):
    print( f'Changing User name {self.user.name} to {name}' )
    self.user.name=name
    return self.user.name

  def drop_user(self,name):
    print( f'I am dropping user {self.user.name}'   )
    self.user.name=''
    return self.user.name

class ExpenseService:
  def __init__(self,amountspnt,product):        
      self.__amountspnt=amountspnt        ##Encapsulation
      self.product=product
      self.mydict={}

  def create_expense(self):
    #mydict={}
    self.mydict[self.__amountspnt]=self.product
    return f'Expense created {self.mydict}'

  def show_report(self):
    return f'Expense report {self.mydict}'     

  @property                                       #Getter
  def admin_amountspnt(self):
     return self.__amountspnt

  @admin_amountspnt.setter                        ###Setter
  def admin_amountspnt(self,newamt):
    self.old=self.__amountspnt
    self.__amountspnt=newamt
    self.mydict.update()
    return self.__amountspnt
     
  


user1=User('kunal','Palam','kk@gmail.com')
us1=UserService(user1)
us1.create_user()
print(us1.change_user('sharma'))
print(us1.drop_user('sharma'))

user2=User('Oscar','Palam','k1k@gmail.com')
us2=UserService(user2)
us2.create_user()
print(us2.change_user('Dcosta'))
print(us2.drop_user('Dcosta'))

eps1=ExpenseService(30,'milk')
eps1.create_expense()
print(eps1.show_report())
eps1.admin_amountspnt
eps1.admin_amountspnt=90
eps1.admin_amountspnt

eps2=ExpenseService(60,'Butter')
eps2.create_expense()
print(eps2.show_report())
eps2.admin_amountspnt
eps2.admin_amountspnt=70
eps2.admin_amountspnt
