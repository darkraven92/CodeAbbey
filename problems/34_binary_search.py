import math

def equation(x, a, b, c, d):
  """Calculates the value of the equation for given x and coefficients."""
  return a * x + b * math.sqrt(x**3) - c * math.exp(-x / 50) - d

def binary_search(a, b, c, d):
    """Performs a binary search to find the root of the equation."""
    low = 0
    high = 100
    precision = 1e-7

    while high - low > precision:
      mid = (low + high) / 2
      if equation(mid, a, b, c, d) > 0:
        high = mid
      else:
        low = mid
    return mid

if __name__ == "__main__":
  num_test_cases = int(input())
  results = []

  for _ in range(num_test_cases):
    a, b, c, d = map(float, input().split())
    x = binary_search(a, b, c, d)
    results.append(str(x))

  print(" ".join(results))