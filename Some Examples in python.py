# Q1. To Find Prime Number
# All the odd number are prime number except for 2
# Note : Negative number are not prime or composite

'''
def prime():
    
    if num<=0:    
        print("Please enter a valid number ")
    elif num%2==0 or num==2:   
        print("Given number is a Composite number ")
    else:
        print("Given number is a prime number ")
num = int(input("Please Enter a Value: "))
prime(num)  '''


# Q2. To find Odd Number
# Note : Zero is also a even Number
# Note : Negative number can be Odd or Even

'''
def odd():
    
    if num%2==0:      
        print("Given number is a Even number ")
    else:
        print("Given number is a odd number ")
num = int(input("Please Enter a Value: "))
odd(num)
'''

#Q.3 To check vowel

# Prompt the user to enter a character
char = input("Enter a character: ")

# Check if the character is a vowel
if char in ['a', 'e', 'i', 'o', 'u']:
    print(char, "is a vowel")
else:
    print(char, "is not a vowel")




# Q4. Given number are vowel or not

'''
def vowel(name):
    j = 0
    for i in name:
        if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
            j=j+1
            
    print(" No of Vowels Present are",j)
        
        
name = str(input("Enter the string: "))
new_name = name.lower()
vowel(new_name)
'''


# Q5. Palindrome of an integer

num = 1221
temp = num
reverse = 0
while temp > 0:
    remainder = temp % 10    
    reverse = (reverse * 10) + remainder
    temp = temp // 10
if num == reverse:
  print('Palindrome')
else:
  print("Not Palindrome")