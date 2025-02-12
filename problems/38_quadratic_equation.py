import math

def solve_quadratic_equation(a, b, c):
    """Solves a quadratic equation and returns the roots.

    Args:
        a: The coefficient of x^2.
        b: The coefficient of x.
        c: The constant term.

    Returns:
        A string representing the roots, separated by a space.
    """
    delta = b**2 - 4 * a * c

    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        
        x1 = int(x1)
        x2 = int(x2)
        
        if x1 > x2:
           return f"{x1} {x2}"
        else:
            return f"{x2} {x1}"
    elif delta == 0:
        x = -b / (2 * a)
        x = int(x)
        return f"{x} {x}"
    else:
        real_part = -b / (2 * a)
        imag_part = math.sqrt(-delta) / (2 * a)
        
        real_part = int(real_part)
        imag_part = int(imag_part)
        
        return f"{real_part}+{imag_part}i {real_part}-{imag_part}i"


if __name__ == "__main__":
    num_test_cases = int(input())
    results = []

    for _ in range(num_test_cases):
        a, b, c = map(int, input().split())
        roots = solve_quadratic_equation(a, b, c)
        results.append(roots)

    print("; ".join(results))