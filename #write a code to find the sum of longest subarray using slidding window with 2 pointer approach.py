arr=[1,2,1,0,1,1,0]
k=int(input("Enter slide size k:"))
slow=0
sum=0
maxlen=0

for fast in range(len(arr)):
    sum += arr[fast]
    
    while sum > k:
        sum -= arr[slow]
        slow += 1
        
    maxlen = max(maxlen, fast - slow + 1)

print("Maxlength:", maxlen)