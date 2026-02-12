college=input()
if college=="yes":
    block=input()
    if block=="yes":
        floor=input()
        if floor=="yes":
             class1=input()
             if class1=="yes":
                print("Present in class")
             else:
                print("Present in floor")
        else:
            print("Present in block")
    else:
        print("Present in college")
else:
    print("college bunk")
