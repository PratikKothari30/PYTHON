 #Q.1 Area of triangle
# get the length and width of the rectangle from the user
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# calculate the area of the rectangle
area = length * width

# display the result
print("The area of the rectangle is", area)



# Q.2 Leap year or not
year = int(input("\nEnter a year: "))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")



# Q.3 Swapping 2 variables
# take two variables
x = 5
y = 10

# print the original values
print("\nBefore swapping: x =", x, ", y =", y)

# create a temporary variable and swap the values
temp = x
x = y
y = temp

# print the swapped values
print("After swapping: x =", x, ", y =", y)


# Q.4 Simple calculator
# define a function for each operation
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

# get user input
print("\nSelect operation.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# perform the selected operation
if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))

elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))

elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))

elif choice == '4':
    print(num1, "/", num2, "=", divide(num1, num2))

else:
    print("Invalid input")



# Q.5Celcius to farenheit
celsius = float(input("\nEnter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C is equal to {fahrenheit}°F")