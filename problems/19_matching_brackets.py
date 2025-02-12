# Read the number of test cases
num_test_cases = int(input())

# Initialize an empty list to store the results
results = []

# Define a dictionary to match opening and closing brackets
bracket_map = {')': '(', ']': '[', '}': '{', '>': '<'}

# Loop through each test case
for _ in range(num_test_cases):
    # Read the input string
    s = input()

    # Use a stack to track open brackets
    stack = []
    is_valid = True

    # Loop through each character in the string
    for char in s:
        if char in '([{<':
            stack.append(char)
        elif char in ')]}>':
            if not stack or stack[-1] != bracket_map[char]:
                is_valid = False
                break
            else:
                stack.pop() # remove matching bracket if any

    # Check if the stack is empty and if brackets matched correctly
    if is_valid and not stack:
      results.append(1) # valid string
    else:
      results.append(0) # invalid string


# Print the results separated by spaces
print(*results)