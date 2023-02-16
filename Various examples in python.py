'''def login():
    while True:
          username = input("Enter Your Username :")
          password = input("Enter Your Password  :")
          if username == password:
           print("Login Successfully")
           break
          else:
            print("You have entered wrong Credentials")
login()'''

#function definition
'''import time
def msg():
    print("Hello World")
    
msg()
time.sleep(2)
msg() 
time.sleep(2)
msg()'''

'''import time
def welcome():
    print("Welcome to Python Class")
    
print('First time call')
welcome()
time.sleep(2)
print('Second time Call')
welcome()
time.sleep(2)
print('third time call')
welcome()
print('Fourth time call')
welcome()'''

'''def info(Firstname,Lastname):
    print('First name =',Firstname)
    print('Last name =',Lastname)
    
info('Prahant','Jha')

def addition(value):
     print("Addition of Two numbers :",value+value)
     
addition(5) ''' 

#positional argument passing in correct order
'''def add(num1,num2):
    result = num1 + num2
    print(f"Result of {num1} and {num2}=",result)

num1 = int(input("Enter 1st value :"))
num2 = int(input("Enter 2st value :"))

add(num1, num2)'''

'''def arithmetic(a,b):
    r = a + b
    n = a * b
    m = a - b
    return r,n,m
    
result = arithmetic(10,5)
print("Result =",result)  '''

'''def chk_even_odd(number):
    if number%2 ==0:
        print(number,"This is Even Number")
    else:
        print(number,"This is Odd Number")
chk_even_odd(5)
chk_even_odd(10)  '''

#default Argument
'''def func(city = "Nagpur"):
    print("I am from ",city)

func(city = "Delhi")
func(city = "LA")
func()      '''

#unknown argument
'''def func(**name):
    print("My name is :",name["Lastname"])
    
func(Firstname = "prashant" , Lastname = "Jha")'''

#returning multiple value at a time
'''def add_product(a,b):
    add = a + b
    product = a * b
    return add,product

x,y = add_product(100,50)
print("The add is :",x)
print("The product is :",y)'''

'''def func(name):
 for i in name:
    print(i)

name_of_p = "prashant"
func(name_of_p)'''

def func(name):
  j=0
  for i in name:
    if i=='n':
      print("The character 'n' is present at index no",j,"value is :",name)
      break
    j=j+1
name=input("Enter the name :")  #prashant
func(name)    
