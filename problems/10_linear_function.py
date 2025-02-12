# Read the number of test cases
num_test_cases = int(input())

# Initialize an empty list to store the results
results = []

# Loop through each test case
for _ in range(num_test_cases):
    # Read the four numbers as a string and split into four values
    values_str = input().split()

    # Convert the numbers to integers
    x1 = int(values_str[0])
    y1 = int(values_str[1])
    x2 = int(values_str[2])
    y2 = int(values_str[3])

    # Calculate 'a' using the formula a = (y2 - y1) / (x2 - x1)
    a = (y2 - y1) / (x2 - x1)
    
    # Calculate 'b' using the formula b = y1 - a * x1
    b = y1 - a * x1
    
    # Append the rounded result to the list
    results.append(f"({int(round(a))} {int(round(b))})")


# Print the results separated by spaces
print(*results)