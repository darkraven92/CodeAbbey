def generate_word(seed, length):
    consonants = "bcdfghjklmnprstvwxz"
    vowels = "aeiou"
    word = []
    for i in range(length):
        # Generate the next random number
        seed = (445 * seed + 700001) % 2097152
        if (i + 1) % 2 == 1:
            # Odd position: consonant
            letter_index = seed % 19
            letter = consonants[letter_index]
        else:
            # Even position: vowel
            letter_index = seed % 5
            letter = vowels[letter_index]
        word.append(letter)
    return ''.join(word), seed

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    # First line: number of words and seed
    num_words = int(data[0])
    seed = int(data[1])
    
    # Second line: lengths of words
    lengths = list(map(int, data[2:2 + num_words]))
    
    # Generate words
    words = []
    for length in lengths:
        word, seed = generate_word(seed, length)
        words.append(word)
    
    # Print the words separated by spaces
    print(" ".join(words))

if __name__ == "__main__":
    main()