def insertion(arr,n):
    for i in range(1,n):
        j = i-1
        key = arr[i]
        while (j>=0) and (key<arr[j]):
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key
arr = []
n = int(input("Please enter the size of the array"))
for i in range(n):
    element = int(input(f"Enter the {i} Element"))
    arr.append(element)
    
print("Your Unsorted element",arr)
insertion(arr,n)
print("Your sorted array is",arr)
