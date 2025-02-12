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

    return adjacency

def dijkstra(adjacency, start, N):
    import sys
    INF = sys.maxsize
    distances = [INF] * (N + 1)
    distances[start] = 0

    # Priority queue (node, distance)
    queue = [(start, 0)]

    while queue:
        current_node, current_distance = queue.pop(0)

        # Skip if we've already found a shorter path
        if current_distance > distances[current_node]:
            continue

        # Explore neighbors
        for neighbor, weight in adjacency[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                queue.append((neighbor, distance))

    return distances[1:]  # Return distances for nodes 1 to N

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    # Read N, X0, and S
    N = int(data[0])
    X0 = int(data[1])
    S = int(data[2])
    
    # Generate the graph
    adjacency = generate_graph(N, X0)
    
    # Run Dijkstra's algorithm
    distances = dijkstra(adjacency, S, N)
    
    # Print the result
    print(" ".join(map(str, distances)))

if __name__ == "__main__":
    main()