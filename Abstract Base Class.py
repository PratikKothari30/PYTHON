from abc import ABC, abstractmethod
class Polygon(ABC):  #Abstract class
    #abstract method
    @abstractmethod
    def noofsides(self):
        pass
    
class Triangle(Polygon):
        #overriding abstract method
        def noofsides(self):
            print("Polygo Said : I have 3 Sides")
            
class Pentagon(Polygon):
    #overriding abstract method
    def noofsides(self):
        print("Pentagon Said : I have 5 sides")
        
class Hexagon(Polygon):
    #overriding abstract method
    def noofsides(sides):
        print("Hexagon said : I have 6 sides")

class Quadrilateral(Polygon):
    #overriding abstract method
    def noofsides(self):
        print("Quadrilateral Said : I have 4 sides")
        
#Driver code
R = Triangle()
R.noofsides()

K = Quadrilateral()
K.noofsides()

R = Pentagon()
R.noofsides()

K = Hexagon()
K.noofsides()


'''from abc import ABC, abstractmethod
class Programming(ABC):  #Abstract class
    #abstract method
    @abstractmethod
    def noofsides(self):
        pass
    @abstractmethod
    def placement(self):
        pass
    
class Ashish(Programming):
    def training(self):
        print('C, C++, Java')
    def placement(self):
        print('Java Placement')
        

class Ankush(Programming):
    def training(self):
        print('Python | Django')
    def placement(self):
        print('Python Placement')
        
class Pratik(Programming):
    def training(self):
        print('Machine Learning')
    def placement(self):
        print('Data Science Placement')
 
obj1 = Ashish()
obj1.training()
obj1.placement()

obj2 = Ankush()
obj2.training()

obj3 = Pratik()
obj3.training()'''