def reverse_string_inplace(s):
  """Reverses a string in-place.

  Args:
    s: The input string.

  Returns:
    The reversed string.
  """
  s = list(s)  # Convert the string to a list for in-place modification
  left = 0
  right = len(s) - 1

  while left < right:
    s[left], s[right] = s[right], s[left]  # Swap characters
    left += 1
    right -= 1

  return "".join(s) #Convert list back to a string


if __name__ == "__main__":
  input_string = input()
  reversed_string = reverse_string_inplace(input_string)
  print(reversed_string)