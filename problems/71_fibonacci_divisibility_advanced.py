def find_fibonacci_index(M):
    # Compute the smallest k such that F_k ≡ 0 mod M
    a, b = 0, 1  # F_0 = 0, F_1 = 1
    k = 0
    while True:
        a, b = b, (a + b) % M
        k += 1
        if a == 0:
            return k

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    # First line is the number of test cases
    num_test_cases = int(data[0])
    
    # Next line contains the divisors M
    divisors = list(map(int, data[1:num_test_cases + 1]))
    
    # Compute the indices for each divisor
    results = []
    for M in divisors:
        index = find_fibonacci_index(M)
        results.append(str(index))
    
    # Print the results
    print(" ".join(results))

if __name__ == "__main__":
    main()