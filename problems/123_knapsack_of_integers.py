def knapsack_01():
    n = int(input())
    max_weight = int(input())
    items = []
    for _ in range(n):
        w, v = map(int, input().split())
        items.append((w, v))

    dp = [[0 for _ in range(max_weight + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        weight = items[i - 1][0]
        value = items[i - 1][1]
        for w in range(max_weight + 1):
            if weight > w:
              dp[i][w] = dp[i - 1][w]
            else:
              dp[i][w] = max(dp[i-1][w], dp[i-1][w - weight] + value)


    print(dp[n][max_weight])

if __name__ == "__main__":
    knapsack_01()