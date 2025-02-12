def count_paths(grid):
  """Counts the number of paths from the top-left to the bottom-right corner.

  Args:
    grid: A 2D list (list of lists) representing the grid, where '+' is passable
        and 'X' is impassable. The top-left corner is assumed to be '@' and the
        bottom-right is '$'.

  Returns:
    The number of paths from the top-left corner to the bottom-right corner.
  """
  m = len(grid)
  if m == 0:
    return 0
  n = len(grid[0])
  
  #Handle corner cases where start or finish is a pit
  if grid[0][0] == 'X' or grid[m-1][n-1] == 'X':
    return 0
  
  dp = [[0 for _ in range(n)] for _ in range(m)]  # Initialize a DP table
  
  dp[0][0] = 1 # There is one way to reach the starting point
  
  for i in range(m):
    for j in range(n):
        if grid[i][j] == 'X':
            continue # we cannot reach X patches

        if i > 0 and grid[i-1][j] != 'X':
             dp[i][j] += dp[i-1][j] # Add paths from the top cell
        if j > 0 and grid[i][j-1] != 'X':
           dp[i][j] += dp[i][j-1] # Add paths from the left cell

  return dp[m - 1][n - 1]

if __name__ == "__main__":
  m, n = map(int, input().split())
  grid = []
  for _ in range(m):
    row = input().split()
    grid.append(row)

  num_paths = count_paths(grid)
  print(num_paths)