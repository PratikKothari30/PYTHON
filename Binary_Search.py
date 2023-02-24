# Array or List must be SORTED for Binary Searching


lis = [12, 13, 15, 25, 36]

def binary(lis, size, target):
    start = 0
    end = size-1

    while(start < end):
       
        mid = start + (end - start)//2

        if (lis[mid] == target):
            return mid

        elif (lis[mid] < target):
            start = mid + 1

        else:
            end = mid -1 

    return -1

print(binary(lis, 5, 25))