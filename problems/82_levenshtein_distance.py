def levenshtein_distance(s1, s2):
    m = len(s1)
    n = len(s2)
    
    # Create a 2D table to store distances
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Initialize the first row and column
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    # Fill the table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # No cost if characters match
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],    # Deletion
                    dp[i][j - 1],    # Insertion
                    dp[i - 1][j - 1] # Substitution
                )
    
    # The bottom-right corner contains the Levenshtein Distance
    return dp[m][n]

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    # First line: number of test cases
    num_test_cases = int(data[0])
    
    # Next lines: test cases (two words each)
    results = []
    index = 1
    for _ in range(num_test_cases):
        s1 = data[index]
        s2 = data[index + 1]
        index += 2
        
        distance = levenshtein_distance(s1, s2)
        results.append(str(distance))
    
    # Print the results separated by spaces
    print(" ".join(results))

if __name__ == "__main__":
    main()