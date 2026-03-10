#edge cases code 2
''' empty '''
s=input("Enter a string")
if s=="":
    print("Empty")
else:
    print("Length:",len(s))
print(s)
''' single char '''
s=input("Enter a string")
if len(s)<=1:
    print("Palindrome.........")
elif s==s[::+1]:
    print("Palindrome........")
else:
    print(s,"not a palindrome")                