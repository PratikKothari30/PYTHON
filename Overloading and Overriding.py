# In python method overloading is not possible
# If we are trying to declare multiple with same name and diff. number of arguments then Python will always consd. only last method

# --------METHOD OVERLOADING--------


'''class Arithmetic:
    def add(self,a):
        print(a)
    def add(self,a,b):
        print(a+b)
    def add(self,a,b,c):   #Here most recent overloaded method will be considered
        print(a+b+c)
obj = Arithmetic()
#obj.add(10)          #This method call will cause the error 
#obj.add(10,20)
obj.add(1,2,3)       #If we call this method directly then no error will occur
'''


#Construtor overloading


'''class Arithematic:
    def __init__(self):
        print("There is no argument")
    def __init__(self,a):
        print("passing one argument")
    def __init__(self,a,b):                       # As in method overloading this will also conder the most recent method
        print("Passing two arguments")

#obj = Arithematic()                  #This line will cause the error as the most recent method has the 2 arguments
#obj = Arithematic(10)
obj = Arithematic(2,2)                #This will implement the code
'''

# Method overriding concept
class Father:
    def bike(self):
        print("BMW")
    def laptop(self):
        print("Normal Laptop")
class Gaurav(Father):
    def laptop(self):
        print("Not acceptable")
        print("Laptop shoud be Gaming")
obj = Gaurav()
obj.bike()
obj.laptop()
#Constructing Overriding
class Father:
    def __init__(self):
        print("Father timing for breakfast 8.00 am")
class Child(Father):
    def __init__(self):
        print("Child i will not be able to Breakfast at 8.00 am")
obj = Child()
class Father:
    def __init__(self):
        print("Father is at breakfast at 8.00 clock")
class Child(Father):
    def __init__(self):
        print("Child will not be at breakfast at 8.00 clock")
        super().__init__()
obj = Child()