def generate_graph(N, X0):
    A = 445
    C = 700001
    M = 2097152
    X = X0

    # Initialize adjacency list
    adjacency = {i: {} for i in range(1, N + 1)}

    for i in range(1, N + 1):
        for _ in range(2):  # Generate two edges per vertex
            X = (A * X + C) % M
            V = X % N + 1
            X = (A * X + C) % M
            D = X % N + 1

            # Skip self-loops and duplicate edges
            if V == i or V in adjacency[i]:
                continue

            # Add edge (undirected)
            adjacency[i][V] = D
            adjacency[V][i] = D

    # Calculate the sum of weights for each vertex
    sums = []
    for i in range(1, N + 1):
        total = sum(adjacency[i].values())
        sums.append(str(total))

    return " ".join(sums)

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    # Read N and X0
    N = int(data[0])
    X0 = int(data[1])
    
    # Generate the graph and compute the sums
    result = generate_graph(N, X0)
    
    # Print the result
    print(result)

if __name__ == "__main__":
    main()