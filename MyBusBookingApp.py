import logging



class BusBooking:
  __CUSTID=10001
  def __init__(self):
    print(f'Welcome to Book My Bus')

  def createUser(self,name):
    self.name=name
    BusBooking.__CUSTID=BusBooking.__CUSTID+1
    with open('bookticket.txt','a') as createuser:
      createuser.write(name + f" {BusBooking.__CUSTID}" + "\n" )
 
  @classmethod
  def showCustId(cls):
    return f'{BusBooking.__CUSTID}'    

  def showTicket(self,name):
    self.name=name
    with open('bookticket.txt','r') as bookcheck:
      for line in bookcheck:
        if self.name in line:
          print(f'{line}')
        else:
          continue  


logging.basicConfig(filename='/content/myapp.log', level=logging.INFO,format="%(asctime)s - %(levelname)s - %(message)s",
    force=True)
booking1=BusBooking() 
logging.info(f"Custid Created {BusBooking.showCustId()}")
booking1.createUser("kunal")  
booking2=BusBooking() 
logging.info(f"Custid Created {BusBooking.showCustId()}")
booking2.createUser("sharma") 
booking3=BusBooking() 
logging.info(f"Custid Created {BusBooking.showCustId()}")
booking3.createUser("oscar")
booking2.createUser("sharma") 
booking3.showTicket("oscar")
