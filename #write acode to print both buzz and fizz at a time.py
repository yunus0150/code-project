#write acode to print both buzz and fizz in 3 and 5 numbers
for i in range(101):
    if (i%3==0 and i%5==0):
        print("Fizzbuzz")
    if i%5==0:
        print("Buzz")
    elif i%3==0:
        print("Fizz")
    else:
        print(i)                
