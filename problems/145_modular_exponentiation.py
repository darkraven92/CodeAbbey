def solve():
    num_testcases = int(input())
    for _ in range(num_testcases):
        a, b, m = map(int, input().split())
        result = modular_pow(a, b, m)
        print(result, end=" ")
    print()

def modular_pow(base, exponent, modulus):
    """
    Calculates (base^exponent) % modulus efficiently using binary exponentiation.

    Args:
        base: The base number.
        exponent: The exponent.
        modulus: The modulus value.

    Returns:
        The result of (base^exponent) % modulus.
    """
    result = 1
    base = base % modulus
    
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        
        base = (base * base) % modulus
        exponent = exponent // 2
    
    return result
    
if __name__ == "__main__":
    solve()