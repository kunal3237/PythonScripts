#############################
class Student:
  def __init__(self):
    pass

  def __call__(self):     ## To make instance of the class callable, It should have __call__ special function
    pass  


callable(Student)       ##Class is always callable
student1=Student()    
callable(student1)
