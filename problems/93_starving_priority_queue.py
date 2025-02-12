import heapq

def solve():
    N, X0 = map(int, input().split())
    
    A = 445
    C = 700001
    M = 2097152
    
    visitors = []
    
    X = X0
    for t in range(N):
        X = (A * X + C) % M
        starvation_degree = (X % 999) + 1
        visitors.append((starvation_degree, t))
    
    heap = []

    total_discomfort = 0
    feeding_time = 0
    visitor_index = 0
    
    while feeding_time <= 2 * N -2 or len(heap) > 0: 
      
        if feeding_time % 2 == 0:
            if len(heap) > 0:
                max_starvation = heapq.heappop(heap)
                starvation_degree = max_starvation[1]
                arrival_time = max_starvation[2]
                
                personal_discomfort = starvation_degree * (feeding_time - arrival_time)
                total_discomfort += personal_discomfort
        
        if visitor_index < N and feeding_time < N:
            heapq.heappush(heap, (-visitors[visitor_index][0], visitors[visitor_index][0], visitors[visitor_index][1]))
            visitor_index+=1


        feeding_time += 1
    
    print(total_discomfort)
    
solve()