def calculate_blackjack_score(cards):
    """Calculates the Blackjack score for a hand of cards.

    Args:
        cards: A list of strings, where each string represents a card.

    Returns:
        The score as an integer, or the string "Bust" if the score exceeds 21.
    """
    score = 0
    num_aces = 0

    for card in cards:
        if card.isdigit():
            score += int(card)
        elif card in ['T', 'J', 'Q', 'K']:
            score += 10
        elif card == 'A':
            num_aces += 1
            score += 11

    while score > 21 and num_aces > 0:
        score -= 10
        num_aces -= 1

    if score > 21:
        return "Bust"
    else:
        return score


if __name__ == "__main__":
    num_test_cases = int(input())
    results = []
    for _ in range(num_test_cases):
        cards = input().split()
        score = calculate_blackjack_score(cards)
        results.append(str(score))

    print(" ".join(results))