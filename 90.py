import itertools

def Has6or9(s):
  return 6 in s or 9 in s

def IsValidArrangment(cube1, cube2):
  """Returns if all square numbers can be displayed using the numbers
  arranged on cube1 and cube2.
  """
  set1 = set(cube1)
  set2 = set(cube2)

  # 01
  if (0 in set1 and 1 in set2) or (0 in set2 and 1 in set1):
    pass
  else:
    return False

  # 04
  if (0 in set1 and 4 in set2) or (0 in set2 and 4 in set1):
    pass
  else:
    return False

  # 09
  if (0 in set1 and Has6or9(set2)) or (0 in set2 and Has6or9(set1)):
    pass
  else:
    return False

  # 16
  if (1 in set1 and Has6or9(set2)) or (1 in set2 and Has6or9(set1)):
    pass
  else:
    return False

  # 25
  if (2 in set1 and 5 in set2) or (2 in set2 and 5 in set2):
    pass
  else:
    return False

  # 36
  if (3 in set1 and Has6or9(set2)) or (3 in set2 and Has6or9(set1)):
    pass
  else:
    return False

  # 49
  if (4 in set1 and Has6or9(set2)) or (4 in set2 and Has6or9(set1)):
    pass
  else:
    return False

  # 64
  if (Has6or9(set1) and 4 in set2) or (Has6or9(set2) and 4 in set1):
    pass
  else:
    return False

  if (8 in set1 and 1 in set2) or (8 in set1 and 1 in set2):
    pass
  else:
    return False
  return True

answer = 0
for x in itertools.combinations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 6):
  for y in itertools.combinations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 6):
    if IsValidArrangment(x, y):
      answer += 1
print answer
# 1045
