def is_possible(time, x, y, n):
    """Checks if it's possible to print N pages within the given time."""
    pages_x = time // x
    pages_y = time // y
    return pages_x + pages_y >= n


def find_min_time(x, y, n):
    """Finds the minimum time to print N pages using binary search."""
    low = 0
    high = max(x,y) * n  # max time is when all pages are printed with the slowest printer

    result = high
    while low <= high:
      mid = (low+high)//2
      if is_possible(mid,x,y,n):
        result = mid
        high = mid - 1
      else:
        low = mid + 1
    return result

# Read the number of test cases
num_test_cases = int(input())

# Initialize an empty list to store the results
results = []

# Loop through each test case
for _ in range(num_test_cases):
    # Read the values as a string and split into three numbers
    values_str = input().split()

    # Convert the numbers to integers
    x = int(values_str[0])
    y = int(values_str[1])
    n = int(values_str[2])

    # Find the minimum time and append to the results
    min_time = find_min_time(x, y, n)
    results.append(min_time)

# Print the results separated by spaces
print(*results)