def calculate_hint(secret, guess):
    # Count digits in correct positions (X)
    correct_positions = sum(1 for s, g in zip(secret, guess) if s == g)
    
    # Count digits in the wrong positions (Y)
    secret_counts = {}
    guess_counts = {}
    
    # Count occurrences of each digit in secret and guess, excluding correct positions
    for s, g in zip(secret, guess):
        if s != g:
            secret_counts[s] = secret_counts.get(s, 0) + 1
            guess_counts[g] = guess_counts.get(g, 0) + 1
    
    # Calculate "Y" as the minimum overlap between secret and guess counts
    wrong_positions = sum(min(secret_counts.get(digit, 0), guess_counts.get(digit, 0))
                          for digit in guess_counts)
    
    return f"{correct_positions}-{wrong_positions}"

def main():
    # Input parsing
    input_data = input().strip()
    secret, num_guesses = input_data.split()[0], int(input_data.split()[1])
    guesses = input().strip().split()
    
    # Calculate hints for each guess
    hints = [calculate_hint(secret, guess) for guess in guesses]
    
    # Output the hints separated by spaces
    print(" ".join(hints))

if __name__ == "__main__":
    main()
