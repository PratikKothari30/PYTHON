#default value of 6-1=5
'''for i in range(1,6):
   print("I will not copy code Blindly")

for i in range(1,11):
   print(i+2)'''

#a = int(input("Enter any one number and get a table"))
#range(start, stop-1, increment/decrement)

'''for i in range(11):
   print(i)'''

'''mylist=[3,5,6,8,2]
for i in mylist:
   print(i)'''   

#Different types of nput statement
'''a=int(input())
a=int(input(("Enter a number : ")))
a=input("Enter a number : ")'''

#to capitalize,lower,upper the string
s = "Dr.D.Y. Patil College Of Engineering"
print(s.capitalize())
print(s.upper())
print(s.lower())
print(s.title())

'''syntax = for var in object:    (loop work in sequence manner 0,1,2,3,4,5)
    print(var)'''
    
li = ["prashant","Ashish","sandip",55,3.14]
 
for i in li:  #i=1
  print(i)
  
#print("\n Tuple Iteration")
t = ("prashant","Ashish","sandip")
for i in t:  #i=3
  print(i)

#Iterating over a string
'''name = "prashant"
for i in name:  #i=1
print(i)'''

i=2
j=5
for i in range(1,5):
    for j in range(1,5):
     print(i ,end=" ")
print()

container = [2,1,4,5,5,4,4,1,1]
count = 0   #count = 3
even = 0    #even = 1
odd = 0     #odd = 2
for i in container:
    if i==4:
       count = count+1
    elif i==2:
       even = even+1
    elif i==5:
       odd = odd+1

print(count-even)
print(count-odd)

for i in range(1,10):
   print(i)
   if i==5:
      break
   

import time
for i in range(1,5):
   for j in range(1,5):
      time.sleep(2)
      print(i,end=" ") 
print()

    
rollno = [3,5,7,1,11,4,5,2]
for x in rollno:
   if x==2 or x==4 or x==6 or x==8 or x==10:
      print("Which even no. is found ",x)
      break

day = input("Enter Day")
if day == "Saturday" or day=="SUNDAY" or day=='SATURDAY' or day=="sunday":
    print("Weekend")
else:
   print("Working Day")    

a,b,c = [float(x) for x in input("Enter Three numbers").split(',')]
print(a+b+c)

a,b,c = [float(x) for x in input("Enter 3 float numbers :").split(',')]
print(a+b+c)

'''a = eval("10+20+30")
print(a)
a = eval("10*20*30")
print(a)'''

'''a = eval(input("Enter Expression"))
print(a)
a = eval(input("Enter list object"))
sum = 0
for x in a:
   sum = sum+x
print(sum)'''   

s = "Python is object oriented programming language"
print(s.find("Python"))
print(s.find("Java"))
print(s.find("Programming"))

s =("prashant","ashish","sandip")
m = 'l'.join(s)
print(m)