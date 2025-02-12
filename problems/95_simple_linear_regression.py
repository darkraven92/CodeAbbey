def solve():
    # Read the range of years
    start_year, end_year = map(int, input().split())
    
    # Initialize variables for sums
    n = 0
    sum_x = 0
    sum_y = 0
    sum_xy = 0
    sum_x2 = 0
    
    # Read data for each year
    for _ in range(end_year - start_year + 1):
        line = input().strip()
        if not line:
            continue
        parts = line.split()
        year = int(parts[0][:-1])  # Remove the colon
        x = int(parts[1])  # Rainy days
        y = int(parts[2])  # Price
        
        # Update sums
        n += 1
        sum_x += x
        sum_y += y
        sum_xy += x * y
        sum_x2 += x * x
    
    # Calculate slope (K) and intercept (B)
    numerator_k = n * sum_xy - sum_x * sum_y
    denominator_k = n * sum_x2 - sum_x * sum_x
    K = numerator_k / denominator_k
    
    B = (sum_y - K * sum_x) / n
    
    # Print the results with high precision
    print(f"{K:.11f} {B:.11f}")

# Call the function
solve()