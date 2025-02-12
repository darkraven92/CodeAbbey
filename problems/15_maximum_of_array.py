# Read the 300 numbers as a string and split into a list
numbers_str = input().split()

# Convert the string numbers to integers
numbers = [int(num_str) for num_str in numbers_str]

# Initialize max and min with the first number
maximum = numbers[0]
minimum = numbers[0]

# Loop through the numbers, starting from the second one
for i in range(1, len(numbers)):
    # Check if the current number is greater than the current maximum
    if numbers[i] > maximum:
        maximum = numbers[i]

    # Check if the current number is less than the current minimum
    if numbers[i] < minimum:
        minimum = numbers[i]

# Print the maximum and minimum values
print(maximum, minimum)