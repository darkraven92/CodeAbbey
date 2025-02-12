def determine_combination(dice):
    from collections import Counter
    
    # Count the frequency of each dice value
    freq = Counter(dice)
    values = sorted(freq.keys())
    counts = sorted(freq.values(), reverse=True)
    
    # Check for yacht
    if counts == [5]:
        return "yacht"
    
    # Check for four
    if counts == [4, 1]:
        return "four"
    
    # Check for full-house
    if counts == [3, 2]:
        return "full-house"
    
    # Check for three
    if counts == [3, 1, 1]:
        return "three"
    
    # Check for two-pairs
    if counts == [2, 2, 1]:
        return "two-pairs"
    
    # Check for pair
    if counts == [2, 1, 1, 1]:
        return "pair"
    
    # Check for small-straight
    if sorted(dice) == [1, 2, 3, 4, 5]:
        return "small-straight"
    
    # Check for big-straight
    if sorted(dice) == [2, 3, 4, 5, 6]:
        return "big-straight"
    
    # If none of the above, return "none"
    return "none"

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    # First line: number of test cases
    num_test_cases = int(data[0])
    
    # Next lines: test cases (5 dice values each)
    test_cases = []
    for i in range(num_test_cases):
        dice = list(map(int, data[1 + i * 5: 6 + i * 5]))
        test_cases.append(dice)
    
    # Determine the combination for each test case
    results = []
    for dice in test_cases:
        combination = determine_combination(dice)
        results.append(combination)
    
    # Print the results
    print(" ".join(results))

if __name__ == "__main__":
    main()