def solve():
    word_list = load_word_list()
    num_testcases = int(input())
    for _ in range(num_testcases):
        line = input().split()
        word_length = int(line[0])
        letters = line[1:]
        count = count_matching_words(word_list, letters, word_length)
        print(count, end=" ")
    print()

def load_word_list():
    words = []
    with open("words.txt", "r") as f:
        for line in f:
            words.append(line.strip().lower())
    return words

def count_matching_words(word_list, letters, word_length):
    count = 0
    for word in word_list:
        if len(word) == word_length:
            if is_word_subset_of_letters(word, letters):
               count += 1
    return count

def is_word_subset_of_letters(word, letters):
    letter_counts = {}
    for letter in letters:
        letter_counts[letter] = letter_counts.get(letter, 0) + 1
    
    for char in word:
        if char not in letter_counts or letter_counts[char] == 0:
            return False
        letter_counts[char] -= 1
    return True

if __name__ == "__main__":
    solve()