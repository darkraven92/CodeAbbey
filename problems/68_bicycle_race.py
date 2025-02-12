def solve():
  n = int(input())
  for _ in range(n):
    s, a, b = map(int, input().split())
    
    # Time to meet = Distance / Relative speed
    time_to_meet = s / (a + b)
    
    # Distance traveled by first cyclist
    distance_a = a * time_to_meet
    
    print(distance_a, end=" ")
  print()
  
solve()