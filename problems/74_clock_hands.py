import math

def calculate_hand_positions(time):
    # Parse the time
    hour, minute = map(int, time.split(':'))
    
    # Normalize hour to 12-hour format
    hour %= 12
    
    # Calculate angles in degrees
    minute_angle = minute * 6  # 360 degrees / 60 minutes
    hour_angle = hour * 30 + minute * 0.5  # 360 degrees / 12 hours + 0.5 degrees per minute
    
    # Convert angles to radians
    minute_angle_rad = math.radians(minute_angle)
    hour_angle_rad = math.radians(hour_angle)
    
    # Calculate coordinates
    # Minute hand: length = 9
    minute_x = 10 + 9 * math.sin(minute_angle_rad)
    minute_y = 10 + 9 * math.cos(minute_angle_rad)
    
    # Hour hand: length = 6
    hour_x = 10 + 6 * math.sin(hour_angle_rad)
    hour_y = 10 + 6 * math.cos(hour_angle_rad)
    
    return hour_x, hour_y, minute_x, minute_y

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    # First line: number of test cases
    num_test_cases = int(data[0])
    
    # Next lines: test cases
    test_cases = data[1:num_test_cases + 1]
    
    # Calculate positions for each test case
    results = []
    for time in test_cases:
        hour_x, hour_y, minute_x, minute_y = calculate_hand_positions(time)
        results.append(f"{hour_x:.7f} {hour_y:.7f} {minute_x:.7f} {minute_y:.7f}")
    
    # Print the results
    print(" ".join(results))

if __name__ == "__main__":
    main()