
def collatz_steps(x):
    """Calculate the number of steps needed for a number to reach 1 in the Collatz sequence."""
    steps = 0
    while x != 1:
        if x % 2 == 0:  # Even
            x //= 2
        else:  # Odd
            x = 3 * x + 1
        steps += 1
    return steps


if __name__ == "__main__":
    # Read input
    num_cases = int(input())
    test_cases = list(map(int, input().split()))
    
    # Calculate the steps for each test case
    results = [collatz_steps(x) for x in test_cases]
    
    # Print results as a single space-separated line
    print(" ".join(map(str, results)))
