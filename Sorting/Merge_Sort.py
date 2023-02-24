# -----M E R G E S O R T------
# most optimal sorting algorithm
#Python program for Implementation of MergeSort


def mergeSort(arr):
    if len(arr)>1:
        
            #finding the middle value of the array
            mid = len(arr)//2
            
            #Dividing the array elements
            L = arr[:mid]
            
            #into 2 values
            R = arr[mid:]
            
            #Sorting the first half
            mergeSort(L)
            
            #Sorting the second half
            mergeSort(R)
            
            i = j = k = 0
            
            #copy data to temp arrays L[] and R[]
            while i<len(L) and j<len(R):
               if L[i] <= R[j]:
                      arr[k] = L[i]
                      i += 1
               else:
                    arr[k] = R[j]
                    j += 1
               k += 1
               
            #Checking if any element was left
            while i < len(L):
                 arr[k] = L[i]
                 i += 1
                 k += 1
            
            #Right
            while j < len(R):
                 arr[k] = R[j]
                 j += 1
                 k += 1
                 
    #Code to print the list             
    return arr

arr = []

n = int(input("Please enter the Size of the element :"))

for i in range(n):
    element=int(input(f"Enter the {i} element :"))
    arr.append(element)
    
print("\nUnsorted array :",arr)

print("\nSorted Array :",mergeSort(arr))
