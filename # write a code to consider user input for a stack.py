# write a code to consider user input for a stack
stack =[]
size= int(input("Enter the size of the stack: "))
for i in range(size):
    value= int (input("Enter a value"))
    stack.append(value)
print("Stack:",stack)
print("Popped element: ", stack.pop())
print("stack: ", stack)    