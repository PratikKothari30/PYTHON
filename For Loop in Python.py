# 1. Syntax for 'For Loop' --> for i in range(start, end, step)
 # 2. For loop is used when the number of iterations is known before entering the loop.
	 
	
'''for i in range(1,6):    #  --> It means i = 1,2,3,4,5    (end - 1) times it will print
	    print("I will use screenshots only for reference")  '''
	

#Printing Table of 2
'''for i in range(1,11):       # --> It will print table of 2
	    print(i*2)
	    # print(f"2 x {i} =", i*2)'''
	

#Example of For loop using LIST 
''' myList=['Dev', 6, 9, 'Raj', 77]
	for i in myList:
	    print(i) '''
	

#Example of For loop using TUPLE 
'''myTuple=('Dev', 6, 9, 'Raj', 77)
	for i in myTuple:
	    print(i) '''
	

#Example of For loop using STRING 
'''for i in "Devraj" :
	    print(i)'''
	

#Example of For loop using STRING taken from user 
'''name = input("Enter your name : ")
	for i in name:
	    print(i)'''
	

#Example of For loop to print specific character from the given string 
'''a = 'Devraj'
	for i in a :
	    if i=='v':
	        print(i)'''
	

'''for i in range(1,11,2):
	    print(i) '''
	

#Reverse Printing
'''for i in range(10,0,-1) :
	    print(i)
	
	r = range(30,5,-3)      #--> % is excluded
	for i in r :
	    print(i)'''
	

	

# write a code to find total number of VOWELS present in a given String
name = input("Enter your Name : ")
vowel_list = ['a','e','i','o','u']
count = 0
length = len(name)
	

for i in range(0,length):
	    if name[i] in vowel_list :
	        count = count + 1
	
print(f"{count} vowels are there !")