def convert_to_dice_point(random_value):
  """Converts an integer random value to a dice point (1 to 6).

  Args:
    random_value: A non-negative integer representing a random value.

  Returns:
    An integer between 1 and 6, representing a dice point.
  """
  dice_point = (random_value % 6) + 1
  return dice_point


if __name__ == "__main__":
    num_test_cases = int(input())
    results = []

    for _ in range(num_test_cases):
      r1, r2 = map(int, input().split())
      dice1 = convert_to_dice_point(r1)
      dice2 = convert_to_dice_point(r2)
      results.append(str(dice1+dice2))

    print(" ".join(results))