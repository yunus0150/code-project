#write a code to implement insertion in a single linked list
class node:
   def __init__(self,data):
      self.data= data
      self.next= None
def insert_end(head,value):
    new_node= node(value)
    if head is None:
        return new_node
    temp= head
    while temp.next:
        temp= temp.next
    temp.next= new_node
    return head
def print_list(head):
    temp=head
    while temp:
        print(temp.data,end='->')
        temp= temp.next
    print("Tail")
head=None
n=int(input("Enter the number of nodes:"))
for i in range(n):
    val=int(input("Enter value:"))
    head=insert_end(head,val)
print("Single linked list:",print_list(head))              