#Example-1 consist of class, constructor with parameter, static variable.
class college:
    roll_no = 40
    def __init__(self,name,age):
        self.name = name   
        self.age = age

    def print(self):
        print(f"My name is {self.name} and  I am {self.age} years old.")
     
student1 = college("pratik",40)
student2 = college("Devraj",35)

print(student1.name)
print(student1.age)
student1.print()

print(student2.name)
print(student2.age)
student2.print()



#Example-2
class Bike:
    gear = 4            # Static variable 

    def __init__(self, company, color) :
        self.Company = company 
        self.Color = color

    def MyFunc(self, price, torque, average) :
        self.Price = price
        self.Torque = torque
        self.Avg = average
        print("\nCompany Name = ", self.Company)
        print("Color = ", self.Color)
        print("Onroad price = ", self.Price)
        print("Torque = ", self.Torque)
        print("Average = ", self.Avg)
        print("No. of Gears = ", self.gear)


b1 = Bike("Honda", "Black")
b1.MyFunc(75663, "15Nm", "60 kmpl")

print('----------------------------------------------------------------')

Bike.gear = 5                    #--> Accessing Static variable
b2 = Bike("Hero", "Red")
b2.MyFunc(98000, "23Nm", "62 Kmpl")