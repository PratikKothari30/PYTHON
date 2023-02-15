
a=float(input("Enter marks for a :"))
b=float(input("Enter marks for b :"))
c=float(input("Enter marks for c :"))
d=float(input("Enter marks for d :"))

if a>=40 and b>=40 and c>=40 and d>=40:
    print("You are Pass")
else:
    print("You are Fail")    
    
total = a+b+c+d
percentage = total/5.0

print("Total : ", total)
print("Percentagen : ", percentage)