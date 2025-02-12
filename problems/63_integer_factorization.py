import math

def prime_factorization(n):
    """Performs prime factorization of a given integer.

    Args:
        n: The integer to factorize.

    Returns:
        A string representing the prime factors of n, in the form "p1*p2*...".
    """
    factors = []
    d = 2 # start with first prime number

    while d * d <= n: # the loop stops when d is greater than sqrt of n
      while (n % d) == 0: # check if d is divisor and repeatedly divide n by it as much as possible
         factors.append(str(d))
         n //= d  # divide n by the divisor
      d += 1

    if n > 1: # if n is greater than 1 then n itself must be a prime number
        factors.append(str(n))

    return "*".join(factors)

if __name__ == "__main__":
    num_integers = int(input())
    results = []
    for _ in range(num_integers):
        n = int(input())
        factors = prime_factorization(n)
        results.append(factors)
    print(" ".join(results))