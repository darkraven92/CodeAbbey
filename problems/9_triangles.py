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

    # Check the triangle inequality theorem
    if (a + b > c) and (a + c > b) and (b + c > a):
        results.append(1)  # Triangle can be formed
    else:
        results.append(0)  # Triangle cannot be formed

# Print the results separated by spaces
print(*results)