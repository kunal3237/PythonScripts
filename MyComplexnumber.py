### My own created complex data types in Python



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
      return Complex(self.real,imag)
    else:
      imag=-1*self.imag
      return Complex(self.real,imag)
   
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

  def __truediv__(self,other):
    den=other.real**2+other.imag**2     
    othercon=other.conjugate()
    num=self*othercon 
    finalcomp=Complex(num.real/den,num.imag/den)
    return finalcomp


comp1=Complex(-3,-7)
comp2=Complex(4,8)
# print(comp1)
# comp12=comp1*comp2
# print(comp12)
# print(comp1.conjugate())
divcomp=comp1/comp2
print(divcomp)


x=3+7j
y=4+8j
print(x/y)
