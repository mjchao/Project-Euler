import sys

cache = {}

def WaysToSplit(n, k):
  """Number of ways to partition n using piles of at most size k"""
  if n == 1 and k >= 1:
    return 1
  if n == 0 and k >= 0:
    return 1
  if n < k:
    return WaysToSplit(n, n)
  if n < 0:
    print "Something went wrong"
    sys.exit(1)
  if k < 0:
    print "Something went wrong"
    sys.exit(1)
  if (n, k) in cache:
    return cache[(n, k)]

  rtn = 0

  # add a partition of next_pile_size
  for next_pile_size in range(1, min(n, k) + 1):
    rtn += WaysToSplit(n - next_pile_size, next_pile_size)

  cache[(n, k)] = rtn
  return rtn

# (1)
print WaysToSplit(1, 1)

# (1, 1)
print WaysToSplit(2, 1)

# (2) or (1, 1)
print WaysToSplit(2, 2)

# (1, 1, 1)
print WaysToSplit(3, 1)

# (2, 1) or (1, 1, 1)
print WaysToSplit(3, 2)

# (3) or (2, 1) or (1, 1, 1)
print WaysToSplit(3, 3)

print WaysToSplit(5, 5)

i = 1
while i < 2000:
  test = WaysToSplit(i, i)
  print i, test
  if test % 1000000 == 0:
    print "Answer:", i, test
    break
  i += 1
#print WaysToSplit(200, 200)
