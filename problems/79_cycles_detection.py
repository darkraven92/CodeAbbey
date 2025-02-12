def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)
    if root_x == root_y:
        return True  # Cycle detected
    if rank[root_x] > rank[root_y]:
        parent[root_y] = root_x
    elif rank[root_x] < rank[root_y]:
        parent[root_x] = root_y
    else:
        parent[root_y] = root_x
        rank[root_x] += 1
    return False  # No cycle detected

def has_cycle(roads):
    parent = {}
    rank = {}
    for road in roads:
        a, b = road.split('-')
        if a not in parent:
            parent[a] = a
            rank[a] = 1
        if b not in parent:
            parent[b] = b
            rank[b] = 1
        if union(parent, rank, a, b):
            return True  # Cycle detected
    return False  # No cycle detected

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    # First line: number of test cases
    num_test_cases = int(data[0])
    
    # Next lines: test cases
    results = []
    index = 1
    for _ in range(num_test_cases):
        num_roads = int(data[index])
        roads = data[index + 1: index + 1 + num_roads]
        index += 1 + num_roads
        
        if has_cycle(roads):
            results.append('1')
        else:
            results.append('0')
    
    # Print the results separated by spaces
    print(" ".join(results))

if __name__ == "__main__":
    main()