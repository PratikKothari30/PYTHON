#The special variable __name__:
#For every python program , a special variable __name__ will be added internally.
# an individual program or as a module.
#If the program executed as an individual program then the value of this variable is __main__

'''def call():
   if __name__ == '__main__':
       print("This is executed as a individual program")
   else:
       print("This is executed as amodule from some other program")
call()'''


#variable length argument
def name(*name):
    print(name)

    name("Ashish","prashant","Tushar",1001)


#Lambda
#Lambda arguments : expression

x = lambda a : a + 10
print(x(5))

x = lambda a,b : a * b
print(x(5,6))

def myfunc(n):
    return lambda a,b : (a+b) * n

mydoubler = myfunc(2)

print(mydoubler(11,12))

x = lambda a,b,c : a + b + c
print(x(5,6,2))