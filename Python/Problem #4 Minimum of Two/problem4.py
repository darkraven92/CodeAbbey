c = []

data = int(input("data:\n"))

for i in range(data):
    x,y = input().split()
    if int(x) < int(y):
        c.append(x)
    else:
        c.append(y)

for u in c:
    print(u, end =" ")
