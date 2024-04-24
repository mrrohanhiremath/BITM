# Python Program to Create and Display Linked List

# Create a node

class Node:
    def __init__(self, data):
       self.data = data
       self.next = None
       
#create a head node and set as null. Here dont be use null. Be use None 
class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None
# Append the data in last
    def append(self, data):
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next
 
    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end = ' ')
            current = current.next
 
a_llist = LinkedList()
n = int(input('How many elements would you like to add? '))
for i in range(n):
    data = int(input('Enter data item: '))
    a_llist.append(data)
print('The linked list: ', end = '')
a_llist.display()

