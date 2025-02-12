def triangle_area(x1, y1, x2, y2, x3, y3):
    """Calculates the area of a triangle using the determinant formula."""
    area = 0.5 * abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2))
    return area

def solve_triangles():
    num_triangles = int(input())
    areas = []

    for _ in range(num_triangles):
        coords = list(map(float, input().split()))
        x1, y1, x2, y2, x3, y3 = coords
        area = triangle_area(x1, y1, x2, y2, x3, y3)
        areas.append(area)

    print(*areas)

if __name__ == "__main__":
    solve_triangles()