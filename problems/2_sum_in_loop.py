# Read the number of values
n = int(input())

# Read the values as a string and split them into a list
values_str = input().split()

# Initialize the sum to 0
total_sum = 0

# Loop through each value, converting to an int and adding to sum
for value_str in values_str:
    value = int(value_str)
    total_sum += value

# Print the final sum
print(total_sum)