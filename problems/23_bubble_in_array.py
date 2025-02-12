# Read the input as a string and split into a list
values_str = input().split()

# Convert the string values to integers and remove -1
values = [int(value_str) for value_str in values_str if value_str != '-1']

# Initialize swap counter
swap_count = 0

# Perform a single bubble sort pass
for i in range(len(values) - 1):
    if values[i] > values[i+1]:
        values[i], values[i+1] = values[i+1], values[i] # Swap values
        swap_count += 1

# Calculate the checksum
checksum = 0
modulus = 10000007
for value in values:
    checksum = (checksum + value) * 113 % modulus

# Print the swap count and the checksum separated by a space
print(swap_count, checksum)