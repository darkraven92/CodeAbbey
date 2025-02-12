def can_queen_take_king(king_pos, queen_pos):
    # Extract row and column for king and queen
    king_col, king_row = king_pos[0], int(king_pos[1])
    queen_col, queen_row = queen_pos[0], int(queen_pos[1])
    
    # Check if they are in the same row, column, or diagonal
    if king_col == queen_col:  # Same column
        return True
    if king_row == queen_row:  # Same row
        return True
    if abs(ord(king_col) - ord(queen_col)) == abs(king_row - queen_row):  # Same diagonal
        return True
    return False

# Read the number of test cases
num_test_cases = int(input())

# Process each test case
results = []
for _ in range(num_test_cases):
    king, queen = input().split()
    if can_queen_take_king(king, queen):
        results.append("Y")
    else:
        results.append("N")

# Print the results separated by spaces
print(" ".join(results))