#####################################Closure######################################
def outer(k):       ### k is passed as parameter to outer funtion
  def inner():
    print(id(k))    ## k has same memory address like global k
    return f"""This is from inner funtion And this is called closure as the varaible from outer function is
    being passed {k()}"""
    
  return inner 

k=lambda: 'lambda function as argument'
print(id(k)) 
s=outer(k)   # This will return inner funtion. Inner function needs to be called 
print(s() )
print(s.__closure__)

###################################Non Closure###################################
def outer(k):       ### k is passed as parameter to outer funtion
  def inner():
    print(id(k))    ## k has same memory address like global k
    return f"""This is from inner funtion And this is called closure as the varaible from outer function is
    being passed {k()}"""
    
  return inner 

k=lambda: 'lambda function as argument'
print(id(k)) 
s=outer(k)   # This will return inner funtion. Inner function needs to be called 
print(s() )
print(s.__closure__)
