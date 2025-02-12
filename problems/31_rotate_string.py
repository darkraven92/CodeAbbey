def rotate_string(k, s):
  """Rotates a string by k characters.

  Args:
    k: The number of characters to rotate (positive for left, negative for right).
    s: The input string.

  Returns:
    The rotated string.
  """
  n = len(s)
  k = k % n  # Handle cases where k > n or k < -n

  s = list(s)  # Convert the string to a list for in-place modification

  if k > 0:  # Left rotation
    for _ in range(k):
      temp = s[0]
      for i in range(n - 1):
        s[i] = s[i + 1]
      s[n - 1] = temp
  elif k < 0:  # Right rotation
    for _ in range(-k):
      temp = s[n - 1]
      for i in range(n - 1, 0, -1):
        s[i] = s[i - 1]
      s[0] = temp
  
  return "".join(s)  # Convert the list back to a string


if __name__ == "__main__":
  num_test_cases = int(input())
  results = []

  for _ in range(num_test_cases):
    k, s = input().split()
    k = int(k)
    rotated_s = rotate_string(k, s)
    results.append(rotated_s)

  print(" ".join(results))