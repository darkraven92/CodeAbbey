import math

def distance_point_to_segment(x1, y1, x2, y2, xp, yp):
    # Calculate the squared length of the segment
    dx = x2 - x1
    dy = y2 - y1
    segment_length_squared = dx * dx + dy * dy

    if segment_length_squared == 0:
        # The segment is a point, return the distance to that point
        return math.hypot(xp - x1, yp - y1)

    # Calculate the projection of the point onto the line
    t = ((xp - x1) * dx + (yp - y1) * dy) / segment_length_squared

    if t < 0:
        # The projection is outside the segment, closer to (x1, y1)
        return math.hypot(xp - x1, yp - y1)
    elif t > 1:
        # The projection is outside the segment, closer to (x2, y2)
        return math.hypot(xp - x2, yp - y2)
    else:
        # The projection is on the segment
        projection_x = x1 + t * dx
        projection_y = y1 + t * dy
        return math.hypot(xp - projection_x, yp - projection_y)

def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    # First line: number of test cases
    num_test_cases = int(data[0])

    # Next lines: test cases (6 values each)
    results = []
    for i in range(num_test_cases):
        x1 = float(data[1 + i * 6])
        y1 = float(data[2 + i * 6])
        x2 = float(data[3 + i * 6])
        y2 = float(data[4 + i * 6])
        xp = float(data[5 + i * 6])
        yp = float(data[6 + i * 6])

        distance = distance_point_to_segment(x1, y1, x2, y2, xp, yp)
        results.append(f"{distance:.7f}")

    # Print the results separated by spaces
    print(" ".join(results))

if __name__ == "__main__":
    main()