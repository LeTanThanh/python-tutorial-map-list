if __name__ == "__main__":
  # Introduction to the Python map() function

  bonuses = [100, 200, 300]
  print(bonuses)

  new_bonuses = []
  for bunus in bonuses:
    new_bonuses.append(bunus * 2)
  print(new_bonuses)

  """
  iterator = map(function, list)
  """

  bonuses = [100, 200, 300]
  print(bonuses)

  def double(bonus):
    return bonus * 2

  iterator = map(double, bonuses)
  print(list(iterator))

  iterator = map(lambda bonus: bonus * 2, bonuses)
  print(list(iterator))
