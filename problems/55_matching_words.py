from collections import Counter

def find_repeated_words(words):
    """Finds and returns words that occur more than once in alphabetical order."""
    # Count occurrences of each word
    word_counts = Counter(words)
    
    # Filter words that appear more than once
    repeated_words = [word for word, count in word_counts.items() if count > 1]
    
    # Sort the repeated words alphabetically
    repeated_words.sort()
    
    return repeated_words


if __name__ == "__main__":
    # Read input
    input_words = input().split()
    
    # Remove the 'end' marker
    input_words.remove("end")
    
    # Find repeated words and print them
    result = find_repeated_words(input_words)
    print(" ".join(result))
