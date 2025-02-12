def solve():
    def initial_board():
        board = [
            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-', '-'],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        ]
        return board

    def move_piece(board, move):
        start_col = ord(move[0]) - ord('a')
        start_row = 8 - int(move[1])
        end_col = ord(move[2]) - ord('a')
        end_row = 8 - int(move[3])

        piece = board[start_row][start_col]
        board[start_row][start_col] = '-'
        board[end_row][end_col] = piece

    def is_valid_pawn_move(board, move):
        start_col = ord(move[0]) - ord('a')
        start_row = 8 - int(move[1])
        end_col = ord(move[2]) - ord('a')
        end_row = 8 - int(move[3])

        piece = board[start_row][start_col]

        if piece == 'P':
            # White pawn
            if end_row >= start_row:
                return False  # Pawns move forward

            if start_col == end_col:
                # Non-capture move
                if board[end_row][end_col] != '-':
                    return False  # Path is blocked

                if start_row - end_row > 2:
                    return False  # Cannot move more than 2 squares

                if start_row - end_row == 2:
                    if start_row != 6:  # First move
                        return False
                    if board[start_row - 1][start_col] != '-':  # Blocked after 1 square
                        return False

            else:
                # Capture move
                if abs(end_col - start_col) != 1 or start_row - end_row != 1:
                    return False  # Invalid diagonal move
                if not board[end_row][end_col].islower():
                    return False  # Must capture a black piece

        elif piece == 'p':
            # Black pawn
            if end_row <= start_row:
                return False  # Pawns move forward

            if start_col == end_col:
                # Non-capture move
                if board[end_row][end_col] != '-':
                    return False  # Path is blocked

                if end_row - start_row > 2:
                    return False  # Cannot move more than 2 squares

                if end_row - start_row == 2:
                    if start_row != 1:  # First move
                        return False
                    if board[start_row + 1][start_col] != '-':  # Blocked after 1 square
                        return False

            else:
                # Capture move
                if abs(end_col - start_col) != 1 or end_row - start_row != 1:
                    return False  # Invalid diagonal move
                if not board[end_row][end_col].isupper():
                    return False  # Must capture a white piece

        else:
            return True  # Not a pawn, always valid

        return True

    def get_piece_color(piece):
        if piece == '-':
            return None
        if piece.isupper():
            return 'white'
        else:
            return 'black'

    num_test_cases = int(input())
    results = []

    for _ in range(num_test_cases):
        moves = input().split()
        board = initial_board()
        incorrect_move = 0
        previous_color = None  # Start with no previous color. First move sets it.

        for i, move in enumerate(moves):
            start_col = ord(move[0]) - ord('a')
            start_row = 8 - int(move[1])
            end_col = ord(move[2]) - ord('a')
            end_row = 8 - int(move[3])

            if board[start_row][start_col] == '-':
                incorrect_move = i + 1
                break

            piece = board[start_row][start_col]
            current_color = get_piece_color(piece)

            if i == 0:
                previous_color = current_color
            elif current_color == previous_color:
                incorrect_move = i + 1
                break

            if piece in ('P', 'p'):
                if not is_valid_pawn_move(board, move):
                    incorrect_move = i + 1
                    break

            move_piece(board, move)
            previous_color = current_color

        results.append(str(incorrect_move))

    print(" ".join(results))

solve()