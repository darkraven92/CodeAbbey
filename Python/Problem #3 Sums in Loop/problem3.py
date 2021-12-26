count = int(input())
sums = []

for i in range(count):
    line = input().split()
    sum = 0
    for num in line:
        sum += int(num)
    sums.append(str(sum))

print(' '.join(sums))
