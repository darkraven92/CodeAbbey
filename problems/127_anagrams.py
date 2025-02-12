def count_anagrams(word, dictionary):
    sorted_word = "".join(sorted(word))
    count = 0
    for dict_word in dictionary:
        if len(dict_word) == len(word):
          if "".join(sorted(dict_word)) == sorted_word:
            if dict_word != word:
              count += 1
    return count

def solve_anagrams():
    dictionary = []
    try:
       with open("words.txt", "r") as f:
         for line in f:
           dictionary.append(line.strip())
    except FileNotFoundError:
        print("Error: words.txt not found")
        return
    except Exception as e:
        print(f"Error reading words.txt: {e}")
        return
    num_cases = int(input())
    results = []
    for _ in range(num_cases):
        word = input()
        anagram_count = count_anagrams(word, dictionary)
        results.append(anagram_count)
    print(*results)

if __name__ == "__main__":
    solve_anagrams()