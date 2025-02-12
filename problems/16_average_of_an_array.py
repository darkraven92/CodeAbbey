# Read the number of test cases
num_test_cases = int(input())

# Initialize an empty list to store the results
results = []

# Loop through each test case
for _ in range(num_test_cases):
    # Read the numbers as a string and split into a list
    numbers_str = input().split()

    # Initialize variables for sum and count
    total_sum = 0
    count = 0

    # Loop through the numbers, convert them to int, and calculate the sum and count
    for num_str in numbers_str:
        num = int(num_str)
        if num == 0:
            break  # End of array
        total_sum += num
        count += 1
    
    # Calculate the average if there is data
    if count > 0:
        average = total_sum / count

        # Round the average using "half away from zero" method
        if average >= 0:
           rounded_average = int(average + 0.5)
        else:
           rounded_average = int(average - 0.5)

        results.append(rounded_average)
    else:
        results.append(0) #If count is zero just store 0 as result

# Print the results separated by spaces
print(*results)