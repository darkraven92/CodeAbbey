# Read M and N
m, n = map(int, input().split())

# Read the array values as a string and split into a list
values_str = input().split()

# Convert the values to integers
values = [int(value_str) for value_str in values_str]

# Initialize an array of counters with zeros
counters = [0] * n

# Loop through the array
for value in values:
    # Increment the corresponding counter (adjust index to start from 0)
    counters[value - 1] += 1

# Print the counters separated by spaces
print(*counters)