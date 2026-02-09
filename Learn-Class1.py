#####################################################
class Seller:
  def __init__(self,name,address,gstin,myinventory=[]):
    self.name=name
    self.address=address
    self.gstin=gstin
    self.myinventory=myinventory


  def addInventory(self,product):
      self.myinventory.append(product)
      return self.myinventory

  def checkInventory(self,product):
      if product in self.myinventory:
        cnt=self.myinventory.count(product)
        return f'Product is available and have Quantity --> {cnt} '    
  def sellProduct(self,product):
    if product in self.myinventory:
      self.myinventory.remove(product)
      return f'self.checkInventory(product) , {self.myinventory}'

s1=Seller('Kunal','Palampur','231213')
s1.addInventory('fan')
s1.addInventory('Table')
s1.addInventory('Almirah')
s1.addInventory('fan')
print(s1.checkInventory('fan'))
print(s1.sellProduct('fan'))
