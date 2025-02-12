import math

def calculate_mean(prices):
    """Calculates the mean of a list of prices."""
    return sum(prices) / len(prices)

def calculate_std_dev(prices, mean):
    """Calculates the standard deviation of a list of prices."""
    variance = sum([(price - mean) ** 2 for price in prices]) / len(prices)
    return math.sqrt(variance)

def is_volatile_enough(prices):
  """Checks if stock is volatile enough based on Paul's rule."""
  mean_price = calculate_mean(prices)
  commission = mean_price * 0.01
  std_dev = calculate_std_dev(prices, mean_price)
  return std_dev >= 4 * commission

if __name__ == "__main__":
    num_stocks = int(input())
    volatile_stocks = []

    for _ in range(num_stocks):
        line = input().split()
        stock_name = line[0]
        prices = list(map(float, line[1:]))

        if is_volatile_enough(prices):
          volatile_stocks.append(stock_name)

    print(" ".join(volatile_stocks))