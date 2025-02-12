from collections import Counter

def generate_combinations_with_repetitions(k, elements):
    """
    Generates combinations of k elements from a set with limited repetitions.

    Args:
        k: The number of elements in each combination.
        elements: A list of elements, possibly with duplicates.

    Returns:
        A list of unique string combinations, sorted lexicographically.
    """

    element_counts = Counter(elements)
    unique_elements = sorted(element_counts.keys())
    counts = [element_counts[elem] for elem in unique_elements]

    num_unique = len(unique_elements)
    result = []
    combination = [0] * k

    def backtrack(index, start_element):
        if index == k:
            result.append("".join(map(str, [unique_elements[i] for i in combination])))
            return

        for i in range(start_element, num_unique):
            if counts[i] > 0:
                combination[index] = i
                counts[i] -= 1
                backtrack(index + 1, i)
                counts[i] += 1

    backtrack(0, 0)
    return sorted(result)


if __name__ == "__main__":
    input_line = input().split(" of ")
    k = int(input_line[0])
    elements = list(map(int, input_line[1].split()))
    
    combinations = generate_combinations_with_repetitions(k, elements)
    print(" ".join(combinations))