#Write a code to find the sum of first 'n' natural numbers using loops

n = int(input("Enter a number : "))
sum = 0
while n > 0:
    sum = sum + n
    n = n-1
print(sum)


#Write a code for Fibonacci Series 
n = int(input("Enter a number :"))
a = 0
b = 1
count = 0

while count < n :
    print(a)
    c = a+b
    a=b
    b=c
    count = count + 1