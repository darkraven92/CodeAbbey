import math

def rotate_star(x, y, angle_degrees):
    angle_radians = math.radians(angle_degrees)
    cos_a = math.cos(angle_radians)
    sin_a = math.sin(angle_radians)
    
    # Rotate the coordinates
    x_new = x * cos_a - y * sin_a
    y_new = x * sin_a + y * cos_a
    
    # Round to the nearest integer
    x_new_rounded = round(x_new)
    y_new_rounded = round(y_new)
    
    return x_new_rounded, y_new_rounded

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    # Read N and A
    N = int(data[0])
    A = float(data[1])
    
    # Read star data
    stars = []
    index = 2
    for _ in range(N):
        name = data[index]
        x = int(data[index + 1])
        y = int(data[index + 2])
        index += 3
        stars.append((name, x, y))
    
    # Rotate each star and store the new coordinates
    rotated_stars = []
    for star in stars:
        name, x, y = star
        x_new, y_new = rotate_star(x, y, A)
        rotated_stars.append((name, x_new, y_new))
    
    # Sort by Y, then by X
    sorted_stars = sorted(rotated_stars, key=lambda s: (s[2], s[1]))
    
    # Extract the names in sorted order
    result = [s[0] for s in sorted_stars]
    
    # Print the result
    print(" ".join(result))

if __name__ == "__main__":
    main()