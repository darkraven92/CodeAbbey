def sieve_of_eratosthenes(limit):
    """Generates a list of prime numbers up to a given limit using Sieve of Eratosthenes.

    Args:
        limit: The upper limit for prime generation (inclusive).

    Returns:
        A list of prime numbers up to the given limit.
    """
    primes = []
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    p = 2
    while p * p <= limit:
        if is_prime[p]:
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False
        p += 1

    for p in range(2, limit + 1):
        if is_prime[p]:
            primes.append(p)
    return primes

def count_primes_in_range(primes, a, b):
  """Counts the number of primes within a range.

  Args:
      primes: A list of prime numbers.
      a: The lower bound of the range.
      b: The upper bound of the range.

  Returns:
      The number of primes in the range [a, b].
  """
  count = 0
  for prime in primes:
    if a <= prime <= b:
        count += 1
    if prime > b: # we can stop the loop if prime is larger than upper bound
        break
  return count
  
if __name__ == "__main__":
    num_pairs = int(input())
    primes = sieve_of_eratosthenes(3000000) # generate primes once for all test cases since they are less than 3M
    results = []
    for _ in range(num_pairs):
        a, b = map(int, input().split())
        count = count_primes_in_range(primes, a, b)
        results.append(str(count))
    print(" ".join(results))