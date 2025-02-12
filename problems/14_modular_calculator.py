# Read the initial number
result = int(input())

# Loop to read and process operations
while True:
    line = input().split()
    operation = line[0]
    value = int(line[1])

    if operation == '+':
        result = (result + value)
    elif operation == '*':
        result = (result * value)
    elif operation == '%':
        modulus = value
        result = result % modulus  # Take the final modulo operation
        break # break when modulo op is found

# Print the final remainder
print(result)