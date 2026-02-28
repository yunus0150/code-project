 #tree recursion / fibonacci series 
def tree(n):
    if n<=1:
        return n
    
    return tree(n+1)+tree(n-2)
n=int(input("Enter a index value:"))
print(tree(n))