### My own created complex data types in Python
x=3+7j
y=4+8j
# sum=x+y
# mulxy=x*y
# print(sum)
# print(x)
# print(mulxy)
# print(x)
# print(type(x))
# print(x.imag)
# print(x.real)
# con=x.conjugate()
# print(con)

class Complex:
  def __init__(self,real,imag):
    self.real=real
    self.imag=imag

  def __str__(self):
    if self.real<0 and self.imag<0:
      return f'({self.real}{self.imag}i)'
    elif self.real>0 and self.imag<0:    
      return f'({self.real}{self.imag}i)'  
    else:
        return f'({self.real}+{self.imag}i)'  
  def conjugate(self):
    if self.imag<0:
      imag=-1*self.imag
      return f'({self.real}+{imag}i)'
    else:
      imag=-1*self.imag
      return f'({self.real}{imag}i)'
   
  def __add__(self,other):
    real=self.real+other.real
    imag=self.imag+other.imag
    if real<0 and imag<0:
      return Complex(real,imag)
    elif real>0 and imag<0:    
      return Complex(real,imag)
    else:
        return Complex(real,imag)
    


  def __mul__(self,other):

    real=self.real*other.real - self.imag*other.imag
    imag=self.real*other.imag +self.imag*other.real
    if real<0 and imag<0:
      return Complex(real,imag)
    elif real>0 and imag<0:    
      return Complex(real,imag)  
    else:
        return Complex(real,imag)


comp1=Complex(3,7)
# print(comp1)
# print(comp1.conjugate())
# print(comp1)
comp2=Complex(4,8)
# compsum=comp1+comp2
# print(compsum)
# print(comp1)
#print(comp2)
# print(comp1.real)
# print(comp1.imag)
print(comp1)
comp12=comp1*comp2
print(comp12)
#print(com)
    # (a + ib) (c + id)
    # (ac − bd) + i(ad + bc)
    # (-12+56)+(-24-28)

x=3+7j
y=4+8j
mulxy=x*y
# print(comp1)
print(mulxy)
