2023-CS1022_ADSA1_B
B
Node and Linked list
Node and Linked list
Indranee Kashyap
•
May 15 (Edited Jun 7)
Node and linked_list
•
100/100
100 points out of possible 100
Due May 15, 11:59 PM
Implement the class Node and class LinkedList

The class LinkedList should have the following method:
append_end() - This method should append a new node at the end of the list
append_begin() - This method should append a new node at the begining of the list
search_node(value) This method should search for a node with the particular value and return true if the node is found and false if the node is not found. (search for the value 4)

new2.py
Text
Class comments
Your work
Graded

problem04.py
Text
Private comments
Assignment details
class Node():
    def __init__(self, value, next):
        self.value = value
        self.next = next


class Linkedlist():
    def __init__(self):
        self.head = Node(0, None)
        one = Node(1, None)
        two = Node(2, None)
        three = Node(3, None)

        self.head.next = one
        one.next = two
        two.next = three

    def print_list(self):
        current = self.head
        while current.next != None:
            print(current.next.value)
            current = current.next

    def append_end(self, value):
        current = self.head
        while current.next != None:
            current = current.next

        new_node = Node(value, None)
        current.next = new_node

    def append_begin(self, value):
        new_node = Node(value, self.head.next)
        self.head.next = new_node

    def search_node(self, value):
        current = self.head.next
        while current != None:
            if current.value == value:
                return True
            current = current.next

        return False


sl = Linkedlist()
sl.append_end(4)
sl.append_begin(5)
sl.print_list()
print(sl.search_node(4))
problem04.py
Displaying problem04.py.
