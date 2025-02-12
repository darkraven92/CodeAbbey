def solve():
    n = int(input())
    
    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
    
    dp[0][0] = 1
    
    for i in range(n+1):
      for j in range(i, n+1):
        if i > 0:
             dp[i][j] += dp[i-1][j]
        if j > i:
             dp[i][j] += dp[i][j-1]
    
    print(dp[n][n])
    
solve()