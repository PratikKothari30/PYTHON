class Nodes:
    #Creating a node
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head=None

#Creating a object of linked list class and assigning a Null value

linked_list = linkedlist() #linked list class constructor will calls automatically

linked_list.head = Nodes(1)
second = Nodes(2)
third = Nodes(3)
#connect nodes
linked_list.head.next = second
second.next = third

#print the linked list item
while linked_list.head != None:
    print(linked_list.head.data, end=" ")
    linked_list.head = linked_list.head.next 


