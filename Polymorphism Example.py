#Polymorphism Example
'''class Principal:
    def role(self):
        print("I am managing all activity of college")

class Dean:
    def role(self):
        print("Dean = I am decision taking person")

class Hod:
    def role(self):
        print("Hod = I have responsibility of teachers and students")
    
class Faculty:
    def responsibility(self):
        print("Faculty = I have to complete syllabus successfully")
#=============class declaration completed======================================
def func(obj):  #called function
    obj.role()  #calling function
campus = [Principal(),Dean(),Hod(),Faculty()]
for obj in campus:
    func(obj)'''

#================Solution for above problem====================================
class Principal:
    def role(self):
        print("I am managing all activity of college")
class Arithmatic:
    def add(self,a):
        print(a)
    def add(self,a,b):
        print(a+b)
    def add(self,a,b,c):
        print(a+b+c)
obj = Arithmatic()
obj.add(10)
obj.add(10,20)
obj.add(1,2,3)

class Dean:
    def role(self):
        print("Dean = I am decision taking person")

def call(obj):   #called function
    if hasattr(obj,'role'):
        obj.role()
    elif hasattr(obj,'order'):
        obj.order()

    obj = Principal()   #creating object of Principal class 1
    call(obj)

    obj = Dean()        #creating object of Principal class 1
    call(obj)
#===============================================================================
'''print('pratik'+'kothari')
print(2+2)
print(2.5+7.5)
#operator overloading
class Deposit:
    def _init_(self,cash):
        self.cash = cash
d1 = Deposit(1000)
d2 = Deposit(2000)
print(d1+d2)'''
'''#magic method available for every operator to overload any operator we have to override that method
class deposit:
    def _init_(self,cash):
        self.cash = cash 
    def _add_(self,other)'''
    
#In python method overloading is not possible
#If we are trying to declare multiple methods with same name and different number of arguments then python will always consider only last method
'''class Arithmatic:
    def add(self,a):
        print(a)
    def add(self,a,b):
        print(a+b)
    def add(self,a,b,c):
        print(a+b+c)
obj = Arithmatic()
obj.add(10)
obj.add(10,20)
obj.add(1,2,3)'''
#=====================================================================================================
#Constructor Overloading
#constructor overloading is not possible in python.
#If we decline multiple constructors then the last constructor will be considered

'''class Arithmatic:
    def __init__(self):
        print("There is no Argument")
    def __init__(self,a):
        print("Passing one Arguments")
    def __init__(self,a,b):
        print("Passing two Arguments")
        
obj = Arithmatic()
obj = Arithmatic(10)
obj = Arithmatic(2,2)'''

#Method overriding concept
class Father:  #parent class
    def bike(self):
        print("Harley Devidson")
    
    def laptop(self):
        print("Laptop with 2GB RAM and 500GB HDD I3 processor")
        
class Aman(Father):   #child class
    def laptop(self):
        print("As per my programming software requirement this is not cool for me")
        print("Laptop with 8GB RAM and 1TB HDD I7 processor")

obj = Aman()
obj.bike()
obj.laptop()
        

class Father:  #parent class
    def bike(self):
        print("Harley Devidson")
    
    def laptop(self):
        print("Laptop with 2GB RAM and 500GB HDD I3 processor")
        
class child(Father):   #child class
    def laptop(self):
        super().laptop()  #here we are calling parent class method using super()
        print("==================================================================")
        print("As per my programming software requirement this is not cool for me")
        print("Laptop with 8GB RAM and 1TB HDD I7 processor")

obj = child()
obj.bike()
obj.laptop()
        