#Python program for Add two numbers
# Ask the user for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Add the numbers together
result = num1 + num2

print("The sum of", num1, "and", num2, "is\n", result)





#calculate maximum number of two numbers
# take input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# compare the numbers and find the maximum
if num1 > num2:
    maximum = num1
else:
    maximum = num2
print("The maximum of", num1, "and", num2, "is\n", maximum)




#Python program to calculate Simple Interest
pa = float(input("Enter Principal amount :  "))
rate = int(input("Enter rate of interest :  "))
Time = float(input("Enter time Duration : "))

SimpleInterest = (pa * rate * Time) / 100

print("Simple Interest = \n" , SimpleInterest)

amount = SimpleInterest + pa

print("Total amount to pay = \n", amount)



#Python program for Compound Interest
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time (in years): "))

CompoundInterest = principal * (1 + rate/100) ** time - principal

print("Compound interest: \n", CompoundInterest )

amount = CompoundInterest  + principal

print("Total amount to pay = \n", amount)



#Python program to calculate Area of circle
import math

# get radius from user
radius = float(input("Enter the radius of the circle: "))

# calculate area using formula A = πr^2
area = math.pi * radius ** 2

print("The area of the circle is: \n", area)