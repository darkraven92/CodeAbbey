def middle_square(start):
    """Simulates the middle-square method and returns the number of iterations to loop."""
    seen = set()
    current = start
    iterations = 0
    while current not in seen:
        seen.add(current)
        squared = str(current * current).zfill(8) # Square and pad with zeros to get 8 chars
        current = int(squared[2:6]) # Get the middle part of 4 chars
        iterations += 1
    return iterations

# Read the number of test cases
num_test_cases = int(input())

# Read the initial numbers as a string and split into a list
initial_values_str = input().split()

# Initialize an empty list to store the results
results = []

# Loop through each initial value
for initial_value_str in initial_values_str:
    # Convert the initial value to an integer
    initial_value = int(initial_value_str)

    # Calculate the number of iterations to loop
    iterations = middle_square(initial_value)

    # Append the number of iterations to the list
    results.append(iterations)


# Print the results separated by spaces
print(*results)