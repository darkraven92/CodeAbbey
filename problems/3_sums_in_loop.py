# Read the number of pairs
num_pairs = int(input())

# Initialize an empty list to store the sums
sums = []

# Loop through each pair
for _ in range(num_pairs):
    # Read the pair as a string and split into two numbers
    pair_str = input().split()

    # Convert the numbers to integers
    num1 = int(pair_str[0])
    num2 = int(pair_str[1])

    # Calculate the sum and add it to the list
    sums.append(num1 + num2)

# Print the sums separated by spaces
print(*sums)