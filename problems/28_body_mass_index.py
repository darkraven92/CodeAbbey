def calculate_bmi_category(weight, height):
  """Calculates the BMI and returns the corresponding category.

  Args:
    weight: Weight in kilograms.
    height: Height in meters.

  Returns:
    The BMI category as a string ('under', 'normal', 'over', 'obese').
  """
  bmi = weight / (height ** 2)

  if bmi < 18.5:
    return "under"
  elif bmi < 25.0:
    return "normal"
  elif bmi < 30.0:
    return "over"
  else:
    return "obese"


if __name__ == "__main__":
  num_people = int(input())
  results = []

  for _ in range(num_people):
    weight, height = map(float, input().split())
    category = calculate_bmi_category(weight, height)
    results.append(category)

  print(" ".join(results))