# Read the length of the array
length = int(input())

# Read the array values as a string and split into a list
values_str = input().split()

# Convert the values to integers
values = [int(value_str) for value_str in values_str]

# Initialize the checksum
checksum = 0
modulus = 10000007

# Loop through the array
for value in values:
    checksum = (checksum + value) * 113 % modulus


# Print the checksum
print(checksum)