def knapsack_01_with_indices():
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
    
    selected_items = []
    current_weight = max_weight
    for i in range(n, 0, -1):
        if dp[i][current_weight] != dp[i-1][current_weight]:
           selected_items.append(i-1)
           current_weight -= items[i-1][0]

    print(*selected_items)

if __name__ == "__main__":
    knapsack_01_with_indices()