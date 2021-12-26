c = []
data = int(input("data:\n"))
for i in range(data):
    c.append(str(min([int(x) for x in input().split()])))

print(" ".join(c))
    

