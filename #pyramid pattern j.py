#pyramid pattern j
n= int(input("Enter size:"))
for i in range(0,n):
    for s in range(0,n-i-1):
        print(" ", end= " ")
    for j in range(0,2*i+1):
        print("j",end=" ")
    print()            
