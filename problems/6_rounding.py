# Read the number of test cases
num_test_cases = int(input())

# Initialize an empty list to store the rounded results
rounded_results = []

# Loop through each test case
for _ in range(num_test_cases):
    # Read the pair as a string and split into two numbers
    pair_str = input().split()

    # Convert the numbers to integers
    num1 = int(pair_str[0])
    num2 = int(pair_str[1])

    # Calculate the division result
    division_result = num1 / num2

    # Round using "half away from zero" method
    if division_result >= 0:
        rounded_result = int(division_result + 0.5)
    else:
        rounded_result = int(division_result - 0.5)

    # Append the rounded result to the list
    rounded_results.append(rounded_result)

# Print the rounded results separated by spaces
print(*rounded_results)