a=["akhil","aravind","jeswanth","prakash"]
print(list(filter(lambda a: a.startswith("a"),a)))

a=["yunusjani403@gmail.com","akhil420@gmail.com","balaji143@gmail.com"]
print(list(filter(lambda a: a.endswith("@gmail.com"),a)))

x="abc143"
print("".join(list(filter(lambda x: x.isalpha(),x))))

x=["akhil","aravind","jeswanth","prakash"]
print(list(map(lambda a:len(x),x)))

