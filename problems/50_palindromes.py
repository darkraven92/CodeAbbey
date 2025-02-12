def is_palindrome(phrase):
    """Check if a phrase is a palindrome."""
    # Normalize the phrase: Remove non-alphanumeric characters and convert to lowercase
    cleaned = ''.join(char.lower() for char in phrase if char.isalnum())
    # Check if the cleaned phrase reads the same forward and backward
    return cleaned == cleaned[::-1]

if __name__ == "__main__":
    # Read input
    num_phrases = int(input())
    phrases = [input().strip() for _ in range(num_phrases)]
    
    # Determine if each phrase is a palindrome
    results = ['Y' if is_palindrome(phrase) else 'N' for phrase in phrases]
    
    # Print results as a space-separated string
    print(" ".join(results))
