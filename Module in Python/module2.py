#import module_name
import module1

#module_name.function_name(parameters)

print(module1.Hello())
module1.square(4)
module1.login("prashant","prashant")
print(module1.pi)

#Second Way

import module1 as m
m.login('prashant','prashant')
m.square(4)
print(m.pi)
print(m.Hello())

#Third Way

#from module_name import function names

from module1 import pi,square,welcome,login,cube,Hello
Hello()
print(pi)
square(4)
print(cube(3))
welcome("Hi","Hello")
login("sss","fff")

#Fourth Way

from module1 import *
Hello()
print(pi)
cube(5)
square(16)
welcome('Pratik','Kothari')
login('xxx','ggg')

from module1 import *
print(pi)
square(45)
Username = str(input("Enter Username"))
Password = str(input("Enter Password"))
login(Username,Password)
