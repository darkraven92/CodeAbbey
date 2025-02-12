def polygon_area(vertices):
    """Calculates the area of a convex polygon using the Shoelace Formula."""
    n = len(vertices)
    area = 0.0
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]  # Wrap around to the first vertex for the last edge
        area += (x1 * y2 - x2 * y1)
    return 0.5 * abs(area)

def solve_polygon():
    num_vertices = int(input())
    vertices = []

    for _ in range(num_vertices):
        x, y = map(float, input().split())
        vertices.append((x, y))

    area = polygon_area(vertices)
    print(area)

if __name__ == "__main__":
    solve_polygon()