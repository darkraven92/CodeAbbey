# Read the number of test cases
num_test_cases = int(input())

# Initialize an empty list to store the results
results = []

# Loop through each test case
for _ in range(num_test_cases):
    # Read the triplet as a string and split into three numbers
    triplet_str = input().split()

    # Convert the numbers to integers
    a = int(triplet_str[0])
    b = int(triplet_str[1])
    c = int(triplet_str[2])

    # Calculate the result of A * B + C
    result = a * b + c

    # Calculate the sum of digits
    digit_sum = 0
    while result > 0:
        digit_sum += result % 10
        result //= 10

    # Append the sum of digits to the list
    results.append(digit_sum)

# Print the results separated by spaces
print(*results)