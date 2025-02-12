def linear_congruential_generator(a, c, m, x0, n):
  """Calculates the n-th member of a linear congruential generator sequence.

  Args:
    a: The multiplier.
    c: The increment.
    m: The modulus.
    x0: The initial value.
    n: The index of the desired member (0-indexed).

  Returns:
    The n-th member of the sequence.
  """

  x_current = x0
  for _ in range(n):
    x_current = (a * x_current + c) % m
  return x_current


if __name__ == "__main__":
  num_test_cases = int(input())
  results = []
  for _ in range(num_test_cases):
    a, c, m, x0, n = map(int, input().split())
    results.append(str(linear_congruential_generator(a, c, m, x0, n)))
  print(" ".join(results))