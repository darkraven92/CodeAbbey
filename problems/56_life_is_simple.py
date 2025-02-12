def count_neighbors(grid, x, y):
    """Counts the number of live neighbors around a cell (x, y)."""
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),         (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]
    count = 0
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == "X":
            count += 1
    return count


def evolve(grid):
    """Simulates one step of the Game of Life."""
    rows, cols = len(grid), len(grid[0])
    # Copy the grid to store the next state
    next_grid = [row[:] for row in grid]

    for x in range(rows):
        for y in range(cols):
            neighbors = count_neighbors(grid, x, y)

            if grid[x][y] == "X":
                # Rule: Dies if it has < 2 or > 3 neighbors
                if neighbors < 2 or neighbors > 3:
                    next_grid[x][y] = "-"
            else:
                # Rule: A new organism is born if it has exactly 3 neighbors
                if neighbors == 3:
                    next_grid[x][y] = "X"

    return next_grid


def count_organisms(grid):
    """Counts the number of live organisms in the grid."""
    return sum(row.count("X") for row in grid)


def main():
    # Read input and initialize the grid
    initial_grid = []
    for _ in range(5):
        initial_grid.append(list(input().strip()))

    # Add padding to prevent boundary issues
    padded_grid = [["-" for _ in range(15)] for _ in range(15)]
    for i in range(5):
        for j in range(7):
            padded_grid[i + 5][j + 4] = initial_grid[i][j]

    # Simulate 5 turns
    organism_counts = []
    for _ in range(5):
        padded_grid = evolve(padded_grid)
        organism_counts.append(count_organisms(padded_grid))

    # Print the result
    print(" ".join(map(str, organism_counts)))


if __name__ == "__main__":
    main()
