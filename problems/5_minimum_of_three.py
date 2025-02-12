# Read the number of triplets
num_triplets = int(input())

# Initialize an empty list to store the minimums
minimums = []

# Loop through each triplet
for _ in range(num_triplets):
    # Read the triplet as a string and split into three numbers
    triplet_str = input().split()

    # Convert the numbers to integers
    num1 = int(triplet_str[0])
    num2 = int(triplet_str[1])
    num3 = int(triplet_str[2])

    # Use nested if-else to find the minimum
    if num1 <= num2:
        if num1 <= num3:
            minimums.append(num1)
        else:
            minimums.append(num3)
    else:
        if num2 <= num3:
            minimums.append(num2)
        else:
            minimums.append(num3)

# Print the minimums separated by spaces
print(*minimums)