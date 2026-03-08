#write acode to reverse an array ds using 2 pointer approach
arr=list(map(int,input("elements:").split()))
left=0
right=len(arr)-1
while left<right:
    arr[left],arr[right]=arr[right],arr[left]
    left+=1
    right-=1
print("Reversed array :",arr)    