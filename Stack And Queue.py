#Stack program
import time
mystack = []  #empty stack to push the element
size = int(input("Enter the size of Stack :"))

for i in range(size):
    a = int(input("Push element in Stack :"))
    mystack.append(a)
else:
    print("Stack is full")
    print(mystack)

print("Pop operation start :")
for i in range(size):
    time.sleep(3)
    print(mystack.pop(),"pop element from stack")
else:
    print("Stack is empty")
    print(mystack)

#PUSH_A(Item)

stack = []
for top in range(5):
    a = int(input("Push a element in Stack :"))
    stack.append(a)
    top += 1
else:
    print("Stack is Full")
    print("Stack =",stack)
    print(" Top =",top)
#=========================================================
for i in range(5):
    print(stack.pop())
    top -= 1
else:
    print("Stack is empty")
    print("Stack =",stack)
    print(" Top =",top)

#Stack is empty , Full or free space

def stack(mylist):
    for top in range(len(mylist)):

        if top>0:
            print("Stack is Full")
            break
        else:
            print("Stack is empty")

mylist = []
stack(mylist)



'''#Queue program
import time
myQueue = []  #Empty Queue
print("Queue Implementation")
print()
size = int(input("Enter the size of Queue :"))

for i in range(size):
    a = int(input("Add item in Queue :"))
    myQueue.append(a)
else:
    print("Queue is Full")
    print("Queue Elements are =",myQueue)

for i in range(size):
    time.sleep(3)
    j=0
    print(myQueue.pop(),":Remove element from Queue")
else:
    print("Queue is empty")
    print("Queue elements are =",myQueue) '''