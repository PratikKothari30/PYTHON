def linear(lis,n,target):   #lis = list name , n = size of list , K = Target element
    
    for i in range(n):
        if (lis[i]==target):
            print(f"Element is found at {i} ")
        else:
            print("Element not found")
            
n = int(input("Enter the size of list :"))
lis = []
for i in range(n):
    element = int(input(f"Enter the {i} element :"))
    lis.append(element)
print(lis)

linear(lis,n,25)


#Linear Search using Flag
'''def linear(lis,n,target):   #lis = list name , n = size of list , K = Target element
    flag=True
    for i in range(n):
        if (lis[i]==target):
             flag=False
    if flag==False:
             print(f"Element is found at {i}")
    else:
            print("Element not found")
            
n = int(input("Enter the size of list"))
lis = []
for i in range(n):
    element = int(input(f"Enter the {i} element"))
    lis.append(element)
print(lis)

linear(lis,n,25)
            '''