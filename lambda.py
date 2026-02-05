### nonlocal and global keywords should be used when there is need to modify the varibles in nested scope. Also do remember LEGB rule

#"""lambda function, For working with lambda function we need to assign it s0me varaible"
# Example with no variable
first_name=lambda : 'kunal'
print(first_name)
fst_name=first_name()

# Example with parameters

last_name=lambda x: fst_name+x
print(last_name)
last_name('sharma')

# Working with kwargs
def chkkwargs(**kwargs):
  mydict=[]
  for keys,values in kwargs.items():
    mydict.append(keys)

  return mydict


chkkwargs(name='rahul', age=22)     ## Parmeters should be passwed like this
####################################################

def func(param):
  """ This is an example of passing a function as a perameter"""
  return param()

def innerfunc():
  return f'This is the function being passed as a parameter'   

k=func(innerfunc)  

#######################################################
def func(param):
  """ This is an example of passing a function as a perameter"""
  print('this will call a function')
  return param

def innerfunc():
  return f'This is the function being passed as a parameter'   

k=func(innerfunc)  
k()

#####################################################
def addition(a,b,*args):
  """function can be assigned to a variable, passed as a parameter and even
  returned as output. That's why these are called first called citizens
  In this example I am passsing *args as collector for all the parameter being passed"""
  sum=0
  sum=a+b
  for i in args:
    sum=sum+i

  return sum

k=addition
k(2,5,7,9,0,9,34,8,21,87)    

$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
def funx1():
  """This is docstring for my function funx1"""
  return f'This is a funtion without parameter'
funx1()  
funx1.__doc__
#####################################################################
x=7
def funscope():
  """varaibles in the local scope will be called, Global scope has least privlies, Scope 
  works on LEGB (Local/enclosed/Glabal/builtnin)"""
  x=5
  return x
funscope()
###########################################################################
def funscope1():
  """ We can view/use the global varaible But can't modify the global variable"""
  return x

funscope1()  

#######################################
def funscope2():
  
  #global x
  x=5
  return x
funscope2()  
print(x)      #### This will throw errror as scope of the variable was limited to local scope, So we will get error

###############################################
def funscope2():
  
  global x
  x=5
  return x
funscope2()  
print(x)                    # this will be ok as be are using global keyword and it will pass the variable globally, with global keyword we can modify the global scope 
                            #variable

############################################################
x=5
def func1():
  x=3
  return x

func1()
print(x)  # this wll print different variables as both have different scopes

#####################################################
#Nested Function
def func2():
  def innerfunc2():
    return f'This is from inner function'
  print( f'This is from outer function')
  return innerfunc2
k=func2() #function innerfunc2 is stored in the variable, Need to call the function  
k()   
#######################################

def outer():
  name='kunal'
  def inner():
    return f'This function is using the variable {name} from outer function'
  return inner  

s=outer()                      #### Outer variable being used by inner function
s()
#############################################
def outer():
  name5='kunal'
  def inner():
    nonlocal name5      ## nonlocal is used for enclosed variable, Immediate outer function. This is used to modify the outer function variable
    name5=name5 + ' Sharma'
    print( f'This function is using the variable {name5} from outer function')
    return name5
  return inner  

s=outer()
s()
################################################
del outer1
def outer1():
  name='sharma'
  def inner1():
    name=name+'palam'          ### THis will make function fail as inner1 function is looking for varaible name, so if you wan to modify the varaible use nonlocal
    return f'This is from inner function {name}'
  print(f'This is from outer function {name}')
  return inner1

l=outer1()
l()

# Below one is working as we are using nonlocal
del outer1
def outer1():
  name='sharma'
  def inner1():
    nonlocal name
    name=name+'palam'
    return f'This is from inner function {name}'
  print(f'This is from outer function {name}')
  return inner1

l=outer1()
l()
