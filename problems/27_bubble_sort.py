def bubble_sort_with_counts(arr):
  """Sorts an array using Bubble Sort and counts passes and swaps.

  Args:
    arr: The array to be sorted.

  Returns:
    A tuple containing (passes, swaps)
  """
  passes = 0
  swaps = 0
  n = len(arr)
  swapped = True  # Initialize to True to enter the loop

  while swapped:
    swapped = False
    passes += 1
    for i in range(n - 1):
      if arr[i] > arr[i + 1]:
        arr[i], arr[i + 1] = arr[i + 1], arr[i]  # Swap using tuple assignment
        swaps += 1
        swapped = True
  
  return passes, swaps


if __name__ == "__main__":
  n = int(input())
  arr = list(map(int, input().split()))
  passes, swaps = bubble_sort_with_counts(arr)
  print(passes, swaps)