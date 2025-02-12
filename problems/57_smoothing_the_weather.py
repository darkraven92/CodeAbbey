def smooth_sequence(sequence):
    """Smooths the sequence by averaging each value with its neighbors."""
    n = len(sequence)
    smoothed = sequence[:]  # Create a copy of the sequence to store smoothed values

    for i in range(1, n - 1):
        smoothed[i] = (sequence[i - 1] + sequence[i] + sequence[i + 1]) / 3

    return smoothed


def main():
    # Read input
    n = int(input().strip())
    measurements = list(map(float, input().strip().split()))

    # Smooth the sequence
    smoothed_sequence = smooth_sequence(measurements)

    # Print the result with a precision of 1e-7
    print(" ".join(f"{x:.7f}" for x in smoothed_sequence))


if __name__ == "__main__":
    main()
