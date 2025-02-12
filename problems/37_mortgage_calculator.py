import math

def calculate_monthly_payment(p, r, l):
    """Calculates the required monthly payment for a mortgage.

    Args:
        p: The principal amount of the loan.
        r: The annual interest rate (in percentage).
        l: The loan term in months.

    Returns:
        The required monthly payment rounded up to the nearest integer.
    """
    r_monthly = r / 100 / 12  # Monthly interest rate in decimal form
    
    if r_monthly == 0:
        return math.ceil(p / l)

    m = (p * r_monthly * (1 + r_monthly)**l) / ((1 + r_monthly)**l - 1)
    return math.ceil(m)


if __name__ == "__main__":
    p, r, l = map(float, input().split())
    monthly_payment = calculate_monthly_payment(p, r, int(l))
    print(monthly_payment)