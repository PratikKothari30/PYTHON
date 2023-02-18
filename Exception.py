'''a = int(input("Enter First Number :"))
b = int(input("Enter Second Number :"))
print(a/b)

a = int(input("Enter first Number :"))
b = int(input("Enter Second Number :"))
try:
   print(a/b)

except:
   print(a/(b+1))'''



'''try:
   a = int(input("Enter first Number :"))
   b = int(input("Enter second Number :"))
   print(a+b)
except:
   print("Enter only decimal value")

print("Welcome to Programming")'''



'''try:
   print(2/0)

except ZeroDivisionError as message:
   print("The Description of exception",message)

a = int(input("Enter the first integer Number :"))
b = int(input("Enter Second integer Number :"))
print(a/b)'''



#multiple excepr block
'''try:
   a = int(input("Enter first integer Number :"))
   b = int(input("Enter the second Number :"))
   print(a/b)
except ZeroDivisionError as message:
   print("Please ensure that you can't Divide any Number by zero :",message)
except ValueError as message:
   print("Enter only integer Number :",message)'''



##Handling multiple different kinds of exception
'''try:
   a = int(input("Enetr first integer Number :"))
   b = int(input("Enter the second Number :"))
   print(a/b)
except (ValueError,ZeroDivisionError) as message:
   print(message)'''



#concept of default except block
'''try:
   a = int(input("Enter the first Number :"))
   b = int(input("Enter the second Number :"))
   print(a/b)
except (ValueError,ZeroDivisionError) as message:
   print("Enter correct number :",message)
except:
   print("This is default part of except block")'''



#Finally block will always executed whether try block generate error or not
'''try:
    a = int(input("Enetr first integer Number :"))
    b = int(input("Enter the second Number :"))
    print(a/b)
except (ValueError,ZeroDivisionError) as message:
   print("Enter correct number :",message)
finally:
   print("I will always executed")'''



#Using try block,except block and finally block
'''try:
    a = int(input("Enetr first integer Number :"))
    b = int(input("Enter the second Number :"))
    print(a/b)
except (ValueError,ZeroDivisionError) as message:
   print("Enter correct number :",message)
finally:
   print("Everything is Ok")'''



#Nested try block
'''try:
   a = int(input("Enter First Number :"))
   b = int(input("Enter second Number :"))
   try:
      print(a/b)
   except ZeroDivisionError as msg:
      print(msg)

except ValueError as msg:
   print(msg)'''



#we can use else block with try,except and finally block
'''try:
   a = int(input("Enter First integer Number :"))
   b = int(input("Enter second integer Number :"))
   print(a/b)
except (ValueError,ZeroDivisionError) as message:
      print(message)
else:
     print("There are no error in try block")
finally:
     print("I am finally block i always executed whether error raise or not")'''



class InterviewEligibal(Exception):
  pass
print(" 1.BE\n 2.Mtech\n 3.BCA\n 4.other\n")

choice = int(input("Enter your choice"))

if choice==1:
    raise InterviewEligibal("You are Eligibal")
elif choice==2:
    raise InterviewEligibal("You are Eligibal")
elif choice==3:
    raise InterviewEligibal("You are Eligibal")
elif choice==4:
    raise InterviewEligibal("You are not Eligibal")
else:
    print("You have entered wrong choice")