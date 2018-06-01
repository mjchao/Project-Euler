

num_ways = {}

def NumWays(width, height):
  if (width, height) in num_ways:
    return num_ways[(width, height)]
  if width <= 0 or height <= 0:
    return 0
  if width == 1 and height == 3:
    return 1
  if width == 2 and height == 3:


  rtn = 0
  # subtract a 2-by-3, which can be built in 2 ways
  rtn += 2 * NumWays(width - 2, height - 3)

  # subtrac a 3-by-2, which can be built in 2 ways
  rtn += 2 * NumWays(width - 3, height - 2)

  # subtract a 1-by-3
  rtn += 1 * NumWays(width - 1, height - 3)
  rtn += 1 * NumWays(width - 3, height - 1)

  num_ways[(width, height)] = rtn
  return rtn
