def rps_winner(match):
    """Determine the winner of a single match."""
    score1 = 0
    score2 = 0
    
    # Define winning conditions
    rules = {
        'RS': 1, 'SP': 1, 'PR': 1,  # First player wins
        'SR': 2, 'PS': 2, 'RP': 2   # Second player wins
    }
    
    # Process each round in the match
    for round_result in match.split():
        if round_result[0] == round_result[1]:
            continue  # It's a draw; no score change
        else:
            winner = rules[round_result]
            if winner == 1:
                score1 += 1
            else:
                score2 += 1
    
    # Determine overall winner
    return 1 if score1 > score2 else 2


if __name__ == "__main__":
    # Read input
    num_matches = int(input())
    matches = [input().strip() for _ in range(num_matches)]
    
    # Determine winners for all matches
    results = [rps_winner(match) for match in matches]
    
    # Print results
    print(" ".join(map(str, results)))
