#Monotonic stack
#write  a code to perform monotonic decreasing  stack and print the range with in
stack=[]
arr=list(map(int,input("Enter a value").split()))
for n in arr:
    while stack and stack[-1]<n:
        stack.pop()
    stack.append(n)
print("Monotonic decreasing stack:", stack)        