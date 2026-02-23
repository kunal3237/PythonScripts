
# Creating my own data types for Fraction

class Fraction:
  def __init__(self,num,den):
    self.num=num
    self.den=den

  def __str__(self):
    return f'{self.num}/{self.den}'


  def __add__(self,other):
     if self.den%other.den==0 or other.den%self.den==0:
       finalnum=self.num
       finalden=self.num + other.num
       finalfact=Fraction(finalnum,finalden)
     else:
        finalden=self.den*other.den
        finalnum=self.num *other.den+ other.num*self.den
        finalfact=Fraction(finalnum,finalden)

     return finalfact

  def __mul__(self,other):
    finalnum=self.num*other.num
    finalden=self.den*other.den
    finalfact=Fraction(finalnum,finalden)
    return finalfact
  
  def __truediv__(self,other):
    finalnum=self.num*other.den
    finalden=self.den*other.num
    finalfact=Fraction(finalnum,finalden)
     
    return  finalfact

  def __sub__(self,other):
     if self.den%other.den==0 or other.den%self.den==0:
       finalnum=self.num
       finalden=self.num - other.num
       finalfact=Fraction(finalnum,finalden)
     else:
        finalden=self.den*other.den
        finalnum=self.num *other.den- other.num*self.den
        finalfact=Fraction(finalnum,finalden)

     return  finalfact   


  def __eq__(self,other):
    if self.num==other.num and self.den==other.den:
      fact1=Fraction(self.num,self.num)
      return f'Both are equal'
    else:
      return f'Both are not equal'  

    


fact1=Fraction(3,4)
fact2=Fraction(6,4)
fact3=Fraction(7,9)
#fact3=Factor(3,4)
# print(fact1)
# print(fact2)
#fact1+fact2
res=fact1+fact3
print(res)
mul=fact1*fact3
print(mul)
div=fact1/fact3
print(div)
min=fact1-fact3
print(min)
fact1==fact3
