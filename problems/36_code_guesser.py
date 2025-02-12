def count_correct_digits(secret, guess):
    """Counts the number of correctly placed digits.

    Args:
        secret: The secret 4-digit number as a string.
        guess: The guessed 4-digit number as a string.

    Returns:
        The number of correctly placed digits.
    """
    count = 0
    for i in range(4):
        if secret[i] == guess[i]:
            count += 1
    return count


def find_secret_number(guesses):
    """Finds the secret number based on the provided guesses and their answers.

    Args:
        guesses: A list of tuples, where each tuple contains a guess (string) and its answer (integer).

    Returns:
        The secret 4-digit number as a string.
    """
    for secret_num in range(1000, 10000):
        secret_num_str = str(secret_num)
        valid = True
        for guess, correct_count in guesses:
            if count_correct_digits(secret_num_str, guess) != correct_count:
                valid = False
                break
        if valid:
            return secret_num_str
    return None


if __name__ == "__main__":
    num_guesses = int(input())
    guesses = []
    for _ in range(num_guesses):
        guess, correct_count = input().split()
        guesses.append((guess, int(correct_count)))

    secret_number = find_secret_number(guesses)
    print(secret_number)