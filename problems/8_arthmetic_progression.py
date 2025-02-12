# Read the number of test cases
num_test_cases = int(input())

# Initialize an empty list to store the sums
sums = []

# Loop through each test case
for _ in range(num_test_cases):
    # Read the triplet as a string and split into three numbers
    triplet_str = input().split()

    # Convert the numbers to integers
    a = int(triplet_str[0])  # First member
    b = int(triplet_str[1])  # Step size
    n = int(triplet_str[2])  # Number of members

    # Calculate the sum of the arithmetic series using the formula
    sum_n = (n * (2 * a + (n - 1) * b)) // 2  # Using integer division

    # Append the sum to the list
    sums.append(sum_n)

# Print the sums separated by spaces
print(*sums)