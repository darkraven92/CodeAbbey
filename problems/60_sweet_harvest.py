def max_candies(candies):
    """Calculates the maximum number of candies the rabbit can collect.

    Args:
        candies: A list of integers representing the number of candies at each isle.

    Returns:
        The maximum number of candies the rabbit can collect.
    """
    n = len(candies)
    if n == 0:
        return 0
    if n == 1:
      return candies[0]
    if n == 2:
       return candies[0]
    dp = [0] * n
    
    dp[0] = candies[0] # Max candies for the first isle is just the candies on the first isle itself.
    dp[1] = candies[0] # Rabbit has to jump over the second isle if there are two isles.
    
    for i in range(2,n):
      # dp[i] stores max candies when rabbit is on ith isle.
        dp[i] = max(dp[i-2], dp[i-3]) + candies[i] # The max candies till i is either max of two or three steps + current candies on isle i
        
    # Rabbit can land on either the last or second last isle. Return the maximum between them.
    return max(dp[n-1], dp[n-2])


if __name__ == "__main__":
    num_test_cases = int(input())
    results = []
    for _ in range(num_test_cases):
      candies = list(map(int, input().split()))
      max_collected = max_candies(candies)
      results.append(str(max_collected))
    print(" ".join(results))