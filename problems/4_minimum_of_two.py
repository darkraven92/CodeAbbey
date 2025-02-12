# Read the number of test cases
num_test_cases = int(input())

# Initialize an empty list to store the minimums
minimums = []

# Loop through each test case
for _ in range(num_test_cases):
    # Read the pair as a string and split into two numbers
    pair_str = input().split()

    # Convert the numbers to integers
    num1 = int(pair_str[0])
    num2 = int(pair_str[1])

    # Use if-else to compare and determine the minimum
    if num1 < num2:
        minimums.append(num1)
    else:
        minimums.append(num2)

# Print the minimums separated by spaces
print(*minimums)