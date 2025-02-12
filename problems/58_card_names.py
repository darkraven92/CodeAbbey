def get_card_name(card_value):
    suits = ['Clubs', 'Spades', 'Diamonds', 'Hearts']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    
    suit_value = card_value // 13  # Integer division to get the suit index
    rank_value = card_value % 13   # Modulus to get the rank index
    
    return f"{ranks[rank_value]}-of-{suits[suit_value]}"

def main():
    # Read the number of cards
    n = int(input().strip())
    
    # Read the card values
    card_values = list(map(int, input().strip().split()))
    
    # Generate the card names
    card_names = [get_card_name(card_value) for card_value in card_values]
    
    # Output the results
    print(" ".join(card_names))

if __name__ == "__main__":
    main()
