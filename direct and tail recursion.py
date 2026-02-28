#using direct/tail recursion print n values
def direct(n):
    if n==-1:
        return
    print(n)
    direct(n-1)
n= int(input("Enter a number :"))
direct(n)    