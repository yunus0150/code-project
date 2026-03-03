x=["python","java","codegnan","gnan"]
l=[]
for i in x:
    l.append(i[0].upper()+i[1:])
print(l)

print(list(map(lambda x:x[0].upper()+x[1:],x)))

print(list(map(lambda x: len(x),x)))

print(list(map(lambda x:x if len(x)>4 else "False",x)))

print(list(map(lambda x:x if "a" in x else "-1",x)))

print(list(map(lambda x:x if "a" not in x else "-1",x)))


