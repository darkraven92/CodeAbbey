# Read the number of test cases
num_test_cases = int(input())

# Read the values as a string and split into a list
values_str = input().split()

# Initialize an empty list to store the results
results = []

# Loop through each value
for value_str in values_str:
    # Convert the value to an integer
    value = int(value_str)

    # Calculate the weighted sum of digits
    weighted_sum = 0
    position = 1
    temp_value = value
    digits = []
    while temp_value > 0:
      digits.insert(0,temp_value%10)
      temp_value //=10
    for digit in digits:
      weighted_sum += digit * position
      position += 1


    # Append the weighted sum to the list
    results.append(weighted_sum)

# Print the results separated by spaces
print(*results)