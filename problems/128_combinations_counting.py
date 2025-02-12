def combinations(n, k):
    # Handle edge cases
    if k == 0 or k == n:
        return 1
    if k > n:
        return 0

    # Minimize the number of multiplications by choosing the smaller of k and n-k
    if k > n - k:
        k = n - k

    # Calculate the result iteratively
    result = 1
    for i in range(k):
        result = result * (n - i) // (i + 1)
    return result

def solve_combinations():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    num_cases = int(data[0])
    results = []
    for i in range(1, 2 * num_cases, 2):
        n = int(data[i])
        k = int(data[i + 1])
        results.append(str(combinations(n, k)))
    
    print(" ".join(results))

if __name__ == "__main__":
    solve_combinations()