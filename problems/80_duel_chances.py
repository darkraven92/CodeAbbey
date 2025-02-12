def alan_win_probability(pA, pB):
    # Convert percentages to probabilities
    pA_prob = pA / 100
    pB_prob = pB / 100
    
    # Calculate the probability of Alan winning
    P_A = pA_prob / (1 - (1 - pA_prob) * (1 - pB_prob))
    
    # Convert back to percentage and round to the nearest integer
    return round(P_A * 100)

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    # First line: number of test cases
    num_test_cases = int(data[0])
    
    # Next lines: test cases (pA and pB)
    results = []
    for i in range(num_test_cases):
        pA = int(data[1 + 2 * i])
        pB = int(data[2 + 2 * i])
        result = alan_win_probability(pA, pB)
        results.append(str(result))
    
    # Print the results separated by spaces
    print(" ".join(results))

if __name__ == "__main__":
    main()