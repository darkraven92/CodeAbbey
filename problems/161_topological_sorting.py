def topological_sort(dependencies):
    """
    Performs topological sorting on a directed acyclic graph (DAG) represented by dependencies.

    Args:
        dependencies: A list of tuples, where each tuple represents a dependency (from, to).
                      For example, ('Wr', 'Mm') means 'Wr' is required for 'Mm'.

    Returns:
        A list of nodes in topological order, or None if the graph contains a cycle.
    """

    graph = {}
    in_degree = {}

    # Build the graph and calculate in-degrees
    for dependency in dependencies:
        from_node, to_node = dependency
        if from_node not in graph:
            graph[from_node] = []
        if to_node not in graph:
            graph[to_node] = []
        graph[from_node].append(to_node)

        if from_node not in in_degree:
            in_degree[from_node] = 0
        if to_node not in in_degree:
            in_degree[to_node] = 0
        in_degree[to_node] += 1

    # Find nodes with in-degree 0 (starting nodes)
    queue = [node for node in in_degree if in_degree[node] == 0]
    
    # Add nodes that are not dependencies
    for dependency in dependencies:
      from_node, to_node = dependency
      if from_node not in in_degree:
        in_degree[from_node] = 0
        queue.append(from_node)
      if to_node not in in_degree:
          in_degree[to_node] = 0
          

    # Perform topological sort using Kahn's algorithm
    result = []
    count = 0
    while queue:
        node = queue.pop(0)
        result.append(node)
        count += 1

        for neighbor in graph.get(node, []):
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Check for cycles
    if count != len(in_degree):
        return None  # Graph has a cycle

    return result


# Read input
num_dependencies = int(input())
dependencies = []
for _ in range(num_dependencies):
    from_node, to_node = input().split()
    dependencies.append((from_node, to_node))

# Perform topological sort
sorted_nodes = topological_sort(dependencies)

# Print the result
if sorted_nodes:
    print(" ".join(sorted_nodes))
else:
    print("Graph has a cycle.")