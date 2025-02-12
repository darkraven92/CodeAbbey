def bezier_point(control_points, alpha):
    # Copy the control points to avoid modifying the original list
    points = [point.copy() for point in control_points]
    
    # Iteratively reduce the points until only one remains
    while len(points) > 1:
        new_points = []
        for i in range(len(points) - 1):
            x = (1 - alpha) * points[i][0] + alpha * points[i + 1][0]
            y = (1 - alpha) * points[i][1] + alpha * points[i + 1][1]
            new_points.append([x, y])
        points = new_points
    
    # Return the final point
    return points[0]

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    # First line: number of control points M and number of alpha values N
    M = int(data[0])
    N = int(data[1])
    
    # Next M lines: control points (X, Y)
    control_points = []
    for i in range(M):
        x = float(data[2 + 2 * i])
        y = float(data[3 + 2 * i])
        control_points.append([x, y])
    
    # Generate N alpha values
    alpha_values = [i / (N - 1) for i in range(N)]
    
    # Compute points on the Bézier curve
    result = []
    for alpha in alpha_values:
        point = bezier_point(control_points, alpha)
        x = round(point[0])
        y = round(point[1])
        result.append(f"{x} {y}")
    
    # Print the results separated by spaces
    print(" ".join(result))

if __name__ == "__main__":
    main()