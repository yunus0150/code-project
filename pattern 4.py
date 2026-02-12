#print *
n=7
for i in range(n):
    for j in range(n):
        if i==j or (i+j)==n-1 or i==n//2 or j==n//2:
            print(" *",end='')
        else:
            print(" ",end='')
    print()