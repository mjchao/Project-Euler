import sys
sys.setrecursionlimit(5000)

cache = {}

def NumSubRectangles(width, height):
  if (width, height) in cache:
    return cache[(width, height)]
  if (height, width) in cache:
    return cache[(height, width)]

  if width == 1 and height == 1:
    return 1

  total = 0
  if width > 1:
    total += NumSubRectangles(width - 1, height) + ((height+1)*(height)/2) * width
  elif height > 1:
    total += NumSubRectangles(width, height - 1) + ((width+1)*(width)/2) * height

  cache[(width, height)] = total
  return total


print NumSubRectangles(1, 2000)

best = 99999
bestDim = None

for i in range(2000):
  for j in range(i+1, 2000):
    num_rect = NumSubRectangles(i, j)
    print i, j, num_rect
    if abs(num_rect - 2000000) < best:
      best = abs(num_rect - 2000000)
      bestDim = (i, j)
    if num_rect > 2000000:
      break

print "ANSWER:", bestDim



