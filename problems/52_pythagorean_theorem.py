def classify_triangle(a, b, c):
    # Calculate squares of the sides
    a_squared = a ** 2
    b_squared = b ** 2
    c_squared = c ** 2

    # Check if the triangle is right-angled, acute-angled, or obtuse-angled
    if c_squared == a_squared + b_squared:
        return "R"  # Right-angled
    elif c_squared < a_squared + b_squared:
        return "A"  # Acute-angled
    else:
        return "O"  # Obtuse-angled

# Read the number of triangles
num_triangles = int(input())

# Process each triangle
results = []
for _ in range(num_triangles):
    # Read the sides of the triangle
    sides = list(map(int, input().split()))
    # Sort the sides to ensure the largest is last
    sides.sort()
    a, b, c = sides
    # Classify the triangle and store the result
    result = classify_triangle(a, b, c)
    results.append(result)

# Print the results separated by spaces
print(" ".join(results))