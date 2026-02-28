# write a code to find the missing number in a series of array
arr=list(map(int,input("Enter values spaces :" ,).split()))
n= len(arr)+1
e_sum= n*(n+1)//2
arr_sum= sum(arr)
print("missing number :", e_sum-arr_sum)