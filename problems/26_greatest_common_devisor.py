def gcd(a, b):
    while b != 0:
        a %= b
        a, b = b, a
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    g = gcd(a, b)
    l = lcm(a, b)
    print(f"({g} {l})", end=" ")
print()
