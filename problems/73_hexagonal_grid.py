import math

def calculate_distance(moves):
    # Define the movement directions in terms of (dx, dy)
    directions = {
        'A': (1, 0),
        'B': (0.5, math.sqrt(3)/2),
        'C': (-0.5, math.sqrt(3)/2),
        'D': (-1, 0),
        'E': (-0.5, -math.sqrt(3)/2),
        'F': (0.5, -math.sqrt(3)/2)
    }
    
    # Start at the origin
    x, y = 0.0, 0.0
    
    # Simulate the moves
    for move in moves:
        dx, dy = directions[move]
        x += dx
        y += dy
    
    # Calculate the Euclidean distance
    distance = math.sqrt(x**2 + y**2)
    return distance

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    # First line: number of test cases
    num_test_cases = int(data[0])
    
    # Next lines: sequences of moves
    sequences = data[1:num_test_cases + 1]
    
    # Calculate distances for each sequence
    distances = []
    for seq in sequences:
        distance = calculate_distance(seq)
        distances.append("{0:.8f}".format(distance).rstrip('0').rstrip('.') or "0.0")
    
    # Print the results
    print(" ".join(distances))

if __name__ == "__main__":
    main()