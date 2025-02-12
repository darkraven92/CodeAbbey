import math

def years_to_reach_target(s, r, p):
    """Calculates the number of years to reach a target sum with annual compounded interest.

    Args:
        s: The starting amount of money.
        r: The required target amount of money.
        p: The annual interest rate (in percentage).

    Returns:
        The number of years it takes to reach the target.
    """
    years = 0
    current_money = s

    while current_money < r:
        # Calculate the balance after one year with annual interest
        current_money = math.floor(current_money * (1 + p / 100) * 100) / 100
        years += 1

    return years


if __name__ == "__main__":
    num_test_cases = int(input())
    results = []

    for _ in range(num_test_cases):
        s, r, p = map(float, input().split())
        years = years_to_reach_target(s, r, p)
        results.append(str(years))

    print(" ".join(results))
