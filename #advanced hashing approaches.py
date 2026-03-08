#advanced hashing approaches
'''
hashing 2 pointer
sliding 2 pointer
'''

#write a code to find all unique quadraples such that a+b+c+d=target in given array
'''
arr=1 0 -1 0 -2 2
target=0
o/p:
    possible quadraplets
    [-2 -1 1 2]=0
    [-2 0 0 2]=0
    [-1 0 0 1]=0
    '''
arr=list(map(int,input("elements:").split()))
target=int(input("target : "))
arr.sort()
n=len(arr)
result=[]
for i in range(n-3):
    if i>0 and arr[i] ==arr[i-1]:
        continue
    for j in range(i+1,n-2):
        if j>i+1 and arr[j]==arr[j-1]:
            continue
        left=j+1
        right=n-1
        while left<right: 
            total=arr[i]+arr[j]+arr[left]+arr[right]
            if total==target:
                result.append([arr[i],arr[j],arr[left],arr[right]])
                left+=1
                right-=1
                while left<right and arr[left]==arr[left-1]:
                    left+=1
                while left<right and arr[right]==arr[right+1]:
                    right-=1
            elif total<target:
                left+=1
            else:
                right-=1
for q in result:
    print(q)