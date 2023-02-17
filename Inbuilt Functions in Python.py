import math
print(math.sqrt(16))
print(math.pi)


import math as m
print(m.sqrt(100))
print(m.pi)

from math import *
print(int(sqrt(36)))
print(ceil(10.1))  #ceil means round of to upper i.e. ceil(10.1)=11
print(floor(23.7)) #floor means round of to down i.e. floor(23.7)=23
print(fabs(-10.8))
print(fabs(23.6))



#To generate random integer between two given numbers(inclusive)

from random import *
for i in range(10):
    print(randint(1,10000))  #randint used for get value in integer

from random import *
for i in range(10):
    print(uniform(1,10))   #uniform used for get value in float
        
        
from random import *
list = ["prashant","rahul","ashish","sandip","pratik","nikhil"]
for i in range(10):
    print(choice(list)
      