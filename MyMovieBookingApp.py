import datetime
from abc import ABC,abstractmethod

class Login(ABC):           ##Abstraction
  
  @abstractmethod           ### Abstractmethod
  def login(self,username,password):
    pass

  @abstractmethod           ### Abstractmethod
  def logout(self):
    pass 

class User(Login):          ### Inheritance
  def __init__(self,username,password):
    self.username=username
    self.password=password

  def login(self,username,password):
    return f'Logged In'

  def logout(self):
    return f'Logged Out'

class BookingApp:           

  __CUSTID=1001        ##Static Attribute
  def __init__(self,user):        #Composition
    self.username=user.username
    self.password=user.password
    BookingApp.__CUSTID=BookingApp.__CUSTID+1
    self.__bookingId=8001

  def bookTicket(self):
    self.__bookingId+=1
    return f'Hi {self.username}, Ticket Booked .. Your ticket number is {self.__bookingId}' 

  def resetTicket(self):
    if self.username=='Admin' and self.password=="1234":
      BookingApp.__CUSTID=1001
    else:
      print("Only Admin can make the required Changes")  
  @property
  def checkCustId(self):
    return f'The current Cust number is {BookingApp.__CUSTID}'







         



### Main File for the Booking App
user1=User("kunal","1234")
user2=User("kunal1","1234")
user3=User("kunal2","1234")
user4=User("Admin","1234")
bookticket=BookingApp(user1)
# bookticket=BookingApp('kunal1','kk2@gmail.com')
# bookticket=BookingApp('kunal2','kk3@gmail.com')
# bookticket=BookingApp('kunal3','kk4@gmail.com')
print('*'*20)
while True:
  print(f"""
  {datetime.datetime.now()}
  Which Movie you want to watch:....
  Please choose from below list
  1) MI4
  2) Titanic
  3) Dil Chahta hai
  4) exit""")
  userInput=int(input("Please enter you choice.... "))
  if userInput==1:
    print(bookticket.bookTicket())
    print(F'Ticket for "MI4" is booked')
  elif userInput==2:
    print(bookticket.bookTicket())
    print(F'Ticket for "Titanic" is booked')
  elif userInput==3:
    print(bookticket.bookTicket())
    print(F'Ticket for "Dil Chahta hai" is booked')
  elif userInput==4:
    print (f'Thanks for using our App. Have a nice day!!')
    break



bookticket.resetTicket()
print(bookticket.checkCustId)
bookticket1=BookingApp(user4)
print(bookticket1.checkCustId)
bookticket1.resetTicket()
print(bookticket1.checkCustId)


