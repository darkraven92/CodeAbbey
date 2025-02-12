# Read input as a string
input_line = input()

# Split the string into two numbers (assuming space as delimiter)
numbers = input_line.split()

# Convert numbers to integers
num1 = int(numbers[0])
num2 = int(numbers[1])

# Calculate the sum
sum_result = num1 + num2

# Print the result
print(sum_result)