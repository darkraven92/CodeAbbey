def check_winner(board):
    """Checks if there is a winner on the board.

    Args:
        board: A list representing the board, where 'X' is player 1, 'O' is player 2, and '-' is empty.

    Returns:
        'X' if player 1 wins, 'O' if player 2 wins, or None if there is no winner.
    """
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]             # Diagonals
    ]
    
    for combination in winning_combinations:
        if board[combination[0]] == board[combination[1]] == board[combination[2]] and board[combination[0]] != '-':
             return board[combination[0]]
        
    return None

def find_winning_move(moves):
  """Finds the move at which the game is won.

  Args:
    moves: A list of integers representing the moves made on the board.

  Returns:
    The move number (1-based index) at which a player wins, or 0 if there is no winner.
  """
  board = ['-'] * 9
  for i, move in enumerate(moves):
     player = 'X' if i % 2 == 0 else 'O'
     board[move - 1] = player
     winner = check_winner(board)
     if winner:
         return i+1 # return 1-based index
  
  return 0 # no winner


if __name__ == "__main__":
    num_test_cases = int(input())
    results = []
    for _ in range(num_test_cases):
        moves = list(map(int, input().split()))
        winning_move = find_winning_move(moves)
        results.append(str(winning_move))
        
    print(" ".join(results))