def sieve_of_eratosthenes(limit):
    """Generates a list of prime numbers up to a given limit using Sieve of Eratosthenes.

    Args:
        limit: The upper limit for prime generation (inclusive).

    Returns:
        A list of prime numbers up to the given limit.
    """
    primes = []
    is_prime = [True] * (limit + 1) # array used for storing which numbers are prime
    is_prime[0] = is_prime[1] = False # 0 and 1 are not primes

    p = 2 # start with the first prime number
    while p*p <= limit: # loop until we processed enough primes
       if is_prime[p]:
           for i in range(p*p, limit + 1, p): # make multiple of prime number to not prime number, which is not optimized with respect to looping only odd numbers and other optimizations
              is_prime[i] = False
       p += 1
    
    for p in range(2,limit + 1):
      if is_prime[p]:
         primes.append(p)
    return primes

if __name__ == "__main__":
    num_primes_to_print = int(input())
    indices = list(map(int, input().split()))

    # Generate the first 200,000 primes (to cover all possible indices)
    primes = sieve_of_eratosthenes(3000000) # 200000th prime is about 2750000, using upper bound 3M which has some safety margin

    output_primes = [str(primes[index - 1]) for index in indices]
    print(" ".join(output_primes))