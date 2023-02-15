#To check entered number is positive negative or zero
a = int(input("Enter any one "))

if a>0:
    print("Your Entered number is positive")
    
if a<0:
    print("Your Entered number is negative")
    
if a == 0:
    print("Your entered number is zero")    
       

#we have to check eligible for driving license or not    
age = int(input("Enter your age : "))
if age >= 18:
    print("You are eligible for Driving License") 
else:
    print("Your are not eligible for Driving License")     
    
#to find greatest number among numbers entered
num1 = int(input("Enter any one number num1 :"))
num2 = int(input("Enter Second number num2 :"))
num3 = int(input("Enter Third number num3 :"))

if num2>num1 and num2>num3:
    print("num2 is Greater Number")

elif num3>num1 and num3>num2:
    print("num3 is Greater number") 
    
else:
    print("num1 is Greater")       