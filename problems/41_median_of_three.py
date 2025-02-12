def find_median(a, b, c):
    """Finds the median of three numbers.

    Args:
        a: The first number.
        b: The second number.
        c: The third number.

    Returns:
        The median (middle) value of the three numbers.
    """
    if (a <= b <= c) or (c <= b <= a):
        return b
    elif (b <= a <= c) or (c <= a <= b):
        return a
    else:
        return c


if __name__ == "__main__":
    num_triplets = int(input())
    medians = []
    for _ in range(num_triplets):
        a, b, c = map(int, input().split())
        median = find_median(a, b, c)
        medians.append(str(median))

    print(" ".join(medians))