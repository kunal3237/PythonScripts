
""" This example showing how we can use the decoratores in python. Decorators 
basically add extra functionality on the the function where it is being aplied
Decorators take function as input and gice function as output."""


def decorator(func):
  """Please note that placing @decorator infront of any function
basically doing this
myhello=decorator(hello)
and at some point this hello will be equal to wrapper and then it is called"""
  def wrapper():
    print('*********')
    return func()
  return wrapper

@decorator
def myhello():
  print('Hi this is decorator testing')

myhello()  
print(decorator.__doc__)

# Normally decoratora are used for logging/security etc

##################################################
#High order Function where a function either takes function as input or return function as output

def myfunc(func,arg):
  return func(arg)

def square(arg):
  return arg**2 

myfunc(square,5)   

