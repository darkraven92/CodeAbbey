# Read the number of test cases
num_test_cases = int(input())

# Initialize an empty list to store the results
results = []

# Loop through each test case
for _ in range(num_test_cases):
    # Read the values as a string and split into two numbers
    values_str = input().split()

    # Convert the numbers to float (for precision)
    x = float(values_str[0])
    n = int(values_str[1])

    # Start with an initial approximation for the square root
    r = 1.0

    # Loop through the steps of the approximation
    for _ in range(n):
      d = x/r
      r = (r + d)/2.0
    # Append the result to the list
    results.append(f"{r:.7f}") # Store formatted result to avoid precision errors


# Print the results separated by spaces
print(*results)