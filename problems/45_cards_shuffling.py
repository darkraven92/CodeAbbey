import random

def shuffle_deck(random_numbers):
    """Shuffle a deck of cards using random numbers provided."""
    # Create the initial deck of cards
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
    suits = ['C', 'D', 'H', 'S']
    deck = [suit + rank for suit in suits for rank in ranks]
    
    # Shuffle the deck using the random numbers
    for i in range(52):
        j = random_numbers[i] % 52  # Restrict to range 0-51 using modulo
        deck[i], deck[j] = deck[j], deck[i]  # Swap the cards
    
    return deck


if __name__ == "__main__":
    # Input: 52 random non-negative integers
    random_numbers = list(map(int, input().split()))
    
    # Shuffle the deck
    shuffled_deck = shuffle_deck(random_numbers)
    
    # Output the shuffled deck as a space-separated string
    print(" ".join(shuffled_deck))
