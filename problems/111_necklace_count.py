import math

def gcd(a, b):
    """Calculates the greatest common divisor of two numbers."""
    while b:
        a, b = b, a % b
    return a

def count_necklaces(b, n):
    """Calculates the number of distinct necklaces using Burnside's Lemma."""
    total = 0
    for k in range(n):
      total += b**gcd(k,n)
    return total//n
    
def solve_necklaces():
    num_cases = int(input())
    results = []
    for _ in range(num_cases):
        b, n = map(int, input().split())
        necklace_count = count_necklaces(b, n)
        results.append(necklace_count)
    print(*results)

if __name__ == "__main__":
    solve_necklaces()