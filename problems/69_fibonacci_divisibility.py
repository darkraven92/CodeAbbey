def solve():
    n = int(input())
    divisors = list(map(int, input().split()))
    
    results = []
    for m in divisors:
        a, b = 0, 1
        index = 1
        while True:
            if a != 0 and a % m == 0:
                results.append(index - 1)
                break
            a, b = b, (a + b) % (m * m)  # Use Pisano period property
            index += 1
            
            # Pisano Period optimization
            if index > 6 * m:
              break
        
    print(*results)

solve()