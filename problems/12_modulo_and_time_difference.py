# Read the number of test cases
num_test_cases = int(input())

# Initialize an empty list to store the results
results = []

# Loop through each test case
for _ in range(num_test_cases):
    # Read the eight numbers as a string and split into eight values
    values_str = input().split()

    # Convert the numbers to integers
    day1 = int(values_str[0])
    hour1 = int(values_str[1])
    min1 = int(values_str[2])
    sec1 = int(values_str[3])
    day2 = int(values_str[4])
    hour2 = int(values_str[5])
    min2 = int(values_str[6])
    sec2 = int(values_str[7])

    # Convert timestamps to seconds from the beginning of the month
    start_seconds = (day1 * 24 * 3600) + (hour1 * 3600) + (min1 * 60) + sec1
    end_seconds = (day2 * 24 * 3600) + (hour2 * 3600) + (min2 * 60) + sec2

    # Calculate the difference in seconds
    diff_seconds = end_seconds - start_seconds

    # Convert the difference back to days, hours, minutes, seconds
    days = diff_seconds // (24 * 3600)
    diff_seconds %= (24 * 3600)
    hours = diff_seconds // 3600
    diff_seconds %= 3600
    minutes = diff_seconds // 60
    seconds = diff_seconds % 60

    # Append the result to the list
    results.append(f"({days} {hours} {minutes} {seconds})")

# Print the results separated by spaces
print(*results)