# Read the number of test cases
num_test_cases = int(input())

# Initialize an empty list to store the results
results = []

# Define a set of vowels
vowels = set('aeiouy')

# Loop through each test case
for _ in range(num_test_cases):
    # Read the input string
    s = input()

    # Initialize vowel counter
    vowel_count = 0

    # Loop through each character in the string
    for char in s:
        if char in vowels:
            vowel_count += 1

    # Append the count to the list
    results.append(vowel_count)

# Print the results separated by spaces
print(*results)