# Program to perform deletion in a Doubly Linked List

class node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class doublyLL:
    def __init__(self):
        self.head = None

    def insert_begin(self, data):
        newnode = node(data)
        if self.head is None:   # corrected None
            self.head = newnode
        else:
            newnode.next = self.head
            self.head.prev = newnode
            self.head = newnode
    def delete_begin(self):
        if self.head is None:
            print("LL is empty!!!")
            return
        self.head=self.head.next
        if self.head:
            self.head.prev=None        

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("Tail")


# Main Program
dll = doublyLL()
n = int(input("Enter the size of DLL: "))

for _ in range(n):
    val = int(input("Enter a value: "))
    dll.insert_begin(val)
print("Before deleting ",dll.display)
dll.delete_begin()
print("After ",dll.display()) 
dll.delete_begin()
print("After ",dll.display())  
dll.delete_begin()
print("After ",dll.display())  