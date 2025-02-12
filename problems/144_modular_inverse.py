def solve():
    num_testcases = int(input())
    for _ in range(num_testcases):
        m, a, b = map(int, input().split())
        x = modular_equation_solver(m, a, b)
        print(x, end=" ")
    print()

def extended_gcd(x, y):
    """
    Calculates the GCD(x, y) and finds the coefficients a and b
    such that ax + by = gcd(x, y) using Extended Euclidean Algorithm.

    Args:
        x: The first integer.
        y: The second integer.

    Returns:
       A tuple (gcd, a, b).
    """
    if x == 0:
        return y, 0, 1
    
    sprev = 1
    scur = 0
    tprev = 0
    tcur = 1
    
    while y != 0:
       q = x // y
       r = x % y
       snext = sprev - q * scur
       tnext = tprev - q * tcur
       
       x = y
       y = r
       sprev = scur
       scur = snext
       tprev = tcur
       tcur = tnext
    
    return x, scur, tcur

def modular_inverse(a, m):
    """
    Calculates the modular inverse of a modulo m.

    Args:
        a: The integer to find the inverse for.
        m: The modulo value.

    Returns:
        The modular inverse of a modulo m or None if no inverse exists.
    """
    gcd, inv, _ = extended_gcd(a, m)
    if gcd != 1:
        return None  # No inverse exists
    
    # Make sure the result is positive
    while inv < 0:
        inv += m
    return inv


def modular_equation_solver(m, a, b):
    """
    Solves the modular equation ax + b = 0 (mod m)

    Args:
       m: the modulo.
       a,b: coefficients

    Returns:
        The solution x, or -1 if no solution exists.
    """
    
    inv_a = modular_inverse(a, m)
    if inv_a is None:
        return -1
    
    x = (-b * inv_a) % m
    return x

if __name__ == "__main__":
    solve()