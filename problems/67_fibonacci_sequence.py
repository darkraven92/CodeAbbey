def generate_fibonacci_numbers(limit):
    """Generates Fibonacci numbers up to a given limit.

    Args:
        limit: The number of Fibonacci numbers to generate.

    Returns:
        A list of tuples, where each tuple contains (Fibonacci number, index).
    """
    fibonacci_numbers = []
    a, b = 0, 1
    fibonacci_numbers.append((a, 0))
    fibonacci_numbers.append((b, 1))
    for i in range(2, limit):
        c = a + b
        fibonacci_numbers.append((c, i))
        a = b
        b = c
    return fibonacci_numbers


if __name__ == "__main__":
    num_fibonacci_numbers = int(input())
    fibonacci_numbers = generate_fibonacci_numbers(1000)
    fibonacci_dict = {num: index for num, index in fibonacci_numbers}  # Store indices by Fibonacci numbers for quick lookup

    results = []
    for _ in range(num_fibonacci_numbers):
        n = int(input())
        results.append(str(fibonacci_dict[n])) # Get indices from dictionary

    print(" ".join(results))