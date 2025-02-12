def solve():
    n = int(input())
    board = [list(map(int, input())) for _ in range(n)]
    num_moves = int(input())
    moves_str = input().split(", ")
    moves = [tuple(map(int, move.split())) for move in moves_str]

    score = 0
    for x, y in moves:
      
        group = find_group(board, x,y)
        if not group:
             continue

        score += len(group) * (len(group) + 1) // 2
        remove_group(board, group)
        apply_gravity(board)
    
    print(score)

def find_group(board, x, y):
    """
    Finds the group of connected cells with the same value.

    Args:
      board: the board of the game
      x, y: coordinates of the cell that was clicked
    
    Returns: list of coordinates of the group, or empty list if the group does not exist
    """
    
    n = len(board)
    if x < 0 or x >= n or y < 0 or y >= n or board[n -1 - y][x] == -1:
      return []
    
    color = board[n-1-y][x]
    group = set()
    visited = set()
    
    def dfs(x, y):
      if (x,y) in visited or x < 0 or x >= n or y < 0 or y >= n or board[n -1 - y][x] != color:
        return
        
      visited.add((x, y))
      group.add((x, y))
      
      dfs(x + 1, y)
      dfs(x - 1, y)
      dfs(x, y + 1)
      dfs(x, y - 1)
    
    dfs(x,y)
    return group

def remove_group(board, group):
    """
    Removes a group of cells from the board.

    Args:
      board: the board of the game
      group: list of coordinates of the group to remove
    """
    n = len(board)
    for x,y in group:
        board[n-1-y][x] = -1

def apply_gravity(board):
    """
    Applies gravity to the board, moving cubes down and shifting columns to the left.

    Args:
      board: the board of the game
    """
    n = len(board)
    
    for col in range(n):
        write_row = n-1
        for row in range(n-1, -1, -1):
            if board[row][col] != -1:
                board[write_row][col] = board[row][col]
                if write_row != row:
                  board[row][col] = -1
                write_row -= 1

    
    new_board = [row[:] for row in board] #Create deep copy to avoid data modification while processing
    write_col = 0
    for col in range(n):
        if all(new_board[row][col] == -1 for row in range(n)):
             continue
        else:
             for row in range(n):
                board[row][write_col] = new_board[row][col]
                if write_col != col:
                   board[row][col] = -1

             write_col += 1

if __name__ == "__main__":
    solve()