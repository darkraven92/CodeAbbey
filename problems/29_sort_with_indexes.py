def sort_and_get_original_indices(arr):
    """Sorts an array and returns the original indices of sorted elements.

    Args:
        arr: The input array of integers.

    Returns:
        A list of integers representing the original indices.
    """

    # Create a list of tuples, where each tuple contains (value, original_index)
    indexed_arr = [(value, index + 1) for index, value in enumerate(arr)]

    # Sort the list of tuples based on the value (the first element of the tuple)
    indexed_arr.sort()

    # Extract the original indices from the sorted tuples
    original_indices = [index for _, index in indexed_arr]

    return original_indices


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    original_indices = sort_and_get_original_indices(arr)
    print(*original_indices)  # Unpack the list when printing