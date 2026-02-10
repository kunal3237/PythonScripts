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




