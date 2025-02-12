def solve():
    # Read the grid
    grid = []
    for _ in range(13):
        row = input().strip().split()
        grid.append(row)
    
    # Initialize the snake
    snake = [(0, 0), (0, 1), (0, 2)]  # Initial positions of the snake's body
    direction = (0, 1)  # Initial direction: right (dx=0, dy=1)
    
    # Parse the moves
    moves = input().strip().split()
    
    # Initialize collision variables
    collision_x, collision_y, collision_step = -1, -1, -1
    step_count = 0
    
    # Simulate the moves
    for i in range(0, len(moves), 2):
        steps = int(moves[i])
        turn = moves[i + 1] if i + 1 < len(moves) else None
        
        for _ in range(steps):
            step_count += 1
            
            # Move the head
            head_x, head_y = snake[-1]
            new_head_x = head_x + direction[0]
            new_head_y = head_y + direction[1]
            
            # Check for collision with itself
            if (new_head_x, new_head_y) in snake:
                collision_x, collision_y = new_head_x, new_head_y
                collision_step = step_count
                break
            
            # Add the new head to the snake
            snake.append((new_head_x, new_head_y))
            
            # Check if the new head is on food
            if grid[new_head_x][new_head_y] == '$':
                # Eat the food: increase length (do not remove the tail)
                grid[new_head_x][new_head_y] = '-'  # Remove food
            else:
                # Remove the tail
                tail_x, tail_y = snake.pop(0)
                grid[tail_x][tail_y] = '-'  # Mark the tail as empty
            
            # Update the grid with the new head
            grid[new_head_x][new_head_y] = 'X'
        
        if collision_step != -1:
            break
        
        # Change direction if a turn is specified
        if turn:
            if turn == 'U':
                direction = (-1, 0)  # Up
            elif turn == 'D':
                direction = (1, 0)   # Down
            elif turn == 'L':
                direction = (0, -1)  # Left
            elif turn == 'R':
                direction = (0, 1)   # Right
    
    # Output the result
    print(f"{collision_y} {collision_x} {collision_step}")

# Call the function
solve()