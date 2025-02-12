def find_path(maze, start_row, start_col):
    """Finds a path from the start to the top-left corner of the maze.

    Args:
        maze: The maze represented as a list of strings.
        start_row: The row of the starting position (0-based).
        start_col: The column of the starting position (0-based).

    Returns:
        The path as a string (e.g., "2D4L2U2L"), or None if no path is found.
    """
    rows = len(maze)
    cols = len(maze[0])
    queue = [(start_row, start_col, "")] # tuples containing row,col and the path
    visited = set()

    while queue:
        row, col, path = queue.pop(0)
        if (row, col) == (0, 0): # target reached
            return path
        if (row, col) in visited: # prevent processing if already visited
            continue
        visited.add((row, col))
        
        moves = [(-1, 0, 'U'), (1, 0, 'D'), (0, -1, 'L'), (0, 1, 'R')] # moves in format (row, col, direction character)
        for move_row, move_col, move_char in moves:
            next_row = row + move_row
            next_col = col + move_col
            if 0 <= next_row < rows and 0 <= next_col < cols and maze[next_row][next_col] == '1': # check for the boundaries and passable cell
                 queue.append((next_row, next_col, path+move_char))# append the next move to the queue

    return None


def compress_path(path):
    """Compresses a path string (e.g., "DDLLLLUULL" to "2D4L2U2L").

    Args:
        path: The path string to compress.

    Returns:
        The compressed path string.
    """
    if not path:
        return ""
    compressed_path = ""
    count = 1
    for i in range(1, len(path)):
        if path[i] == path[i - 1]:
            count += 1
        else:
            compressed_path += str(count) + path[i - 1]
            count = 1
    compressed_path += str(count) + path[-1] # add the last move
    return compressed_path


if __name__ == "__main__":
    width, height = map(int, input().split())
    maze = [input() for _ in range(height)]

    paths = []
    # paths for A B and C
    start_points = [(0, width-1),(height -1,0),(height-1, width-1)]

    for row, col in start_points:
        path = find_path(maze, row, col)
        if path:
          compressed_path = compress_path(path)
          paths.append(compressed_path)
        else:
            paths.append("No path")
    print(" ".join(paths))