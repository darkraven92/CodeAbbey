def josephus_problem(n, k):
  """Solves the Josephus Problem.

  Args:
    n: The number of people.
    k: The counting step.

  Returns:
    The position of the survivor (1-based index).
  """
  people = list(range(1, n + 1))  # Create a list representing the people
  current_index = 0

  while len(people) > 1:
    current_index = (current_index + k - 1) % len(people)
    people.pop(current_index)

  return people[0]


if __name__ == "__main__":
  n, k = map(int, input().split())
  survivor = josephus_problem(n, k)
  print(survivor)