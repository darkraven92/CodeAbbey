import math

def convert_to_dice_point(random_value):
  """Converts a random value in range [0, 1) to a dice point (1 to 6).

  Args:
    random_value: A floating-point number between 0 (inclusive) and 1 (exclusive).

  Returns:
    An integer between 1 and 6, representing a dice point.
  """
  scaled_value = random_value * 6
  dice_point = math.floor(scaled_value) + 1
  return dice_point


if __name__ == "__main__":
  num_values = int(input())
  results = []

  for _ in range(num_values):
    random_value = float(input())
    dice_point = convert_to_dice_point(random_value)
    results.append(str(dice_point))

  print(" ".join(results))