'''class Base: #parent class
    def __init__(self):
        print("Parent class constructor called")
        self._a = 2  #Protected member
#creating a derived class
class Derived(Base): #child class
    def __init__(self):
        #calling constructor of Base class
        Base.__init__(self)
        print("Calling protected member of base class :")
        print(self._a)
        
obj1 = Derived()
print(obj1.a)
obj2 = Base()
#calling protected member
#outside class will result in AttributeError
print(obj2.a)
'''

class Base: #parent class
    def __init__(self):
      print("Parent class constructor called")
      self._a = "YCCE"  #public data member
      self.__c = "IIM"  #private memner
      
#creating a derived class
class Derived(Base):
    def __init__(self):
        
        #calling constructor of Base class
        Base.__init__(self)
        print("Calling protected member of base class :")
        print(self.__c)
#Driver mode
obj1 = Derived()
print(obj1.a)
#print(obj1.c)
obj2 = Base()
print(obj2.a)