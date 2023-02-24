def bubbleSort(arr):
    n = len(arr)

    for i in range(n):


        for j in range(0, n-i-1):

            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1] , arr[j]


n = int(input("enter the length of array"))

arr = []

for i in range(n):
    a  = int(input(f"enter the {i} element of array"))
    arr.append(a)

for i in range(n):
    print(arr[i])
bubbleSort(arr)

print("Sorted array is")

for i in range(len(arr)):
    print(arr[i], end=" ")
