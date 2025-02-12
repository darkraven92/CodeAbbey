def solve():
    num_roads = int(input())
    adj_matrix = {}
    states = set()

    for _ in range(num_roads):
        road = input().split(" - ")
        state1, state2 = road[0], road[1]
        states.add(state1)
        states.add(state2)
        if state1 not in adj_matrix:
          adj_matrix[state1] = {}
        if state2 not in adj_matrix:
          adj_matrix[state2] = {}
        
        adj_matrix[state1][state2] = 1 # undirected graph, adding 1 to mark connection, adding it for both directions
        adj_matrix[state2][state1] = 1


    num_routes = int(input())
    routes = []
    for _ in range(num_routes):
      routes.append(input().split(" - "))

    # convert states to integer indices
    states = list(states)
    num_states = len(states)
    state_to_index = {state: index for index, state in enumerate(states)}

    #Floyd Warshall algorithm for all pairs shortest path
    dist = [[float('inf')] * num_states for _ in range(num_states)]
    for i in range(num_states):
      dist[i][i] = 0
      if states[i] in adj_matrix:
        for neighbor in adj_matrix[states[i]]:
          dist[i][state_to_index[neighbor]] = 1
          
    for k in range(num_states):
      for i in range(num_states):
         for j in range(num_states):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    # calculate the required distances
    results = []
    for route in routes:
      state1, state2 = route[0], route[1]
      index1 = state_to_index.get(state1, None)
      index2 = state_to_index.get(state2, None)
      if index1 is not None and index2 is not None:
         distance = dist[index1][index2]
         if distance == float('inf'):
            results.append(10000000) # if the states are not connected append the specified value
         else:
            results.append(distance)
      else:
         results.append(10000000)

    print(" ".join(map(str, results)))

if __name__ == "__main__":
    solve()