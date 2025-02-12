import math

def find_pythagorean_triple(s):
    # Iterate over possible values of m
    for m in range(1, int(math.sqrt(s // 2)) + 1):
        if (s // 2) % m == 0:  # Check if m divides s/2
            n = (s // (2 * m)) - m
            if n > 0 and m > n:  # Ensure n is positive and m > n
                # Compute a, b, c
                a = m**2 - n**2
                b = 2 * m * n
                c = m**2 + n**2
                # Verify the sum condition
                if a + b + c == s:
                    return c**2
    return -1  # No valid triple found

# Read the number of test cases
num_test_cases = int(input())

# Process each test case
results = []
for _ in range(num_test_cases):
    s = int(input())
    c_squared = find_pythagorean_triple(s)
    results.append(str(c_squared))

# Print the results separated by spaces
print(" ".join(results))