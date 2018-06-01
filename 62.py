from collections import defaultdict
import sys

cache = defaultdict(int)

for i in range(1,1000000):
  cube = i**3
  str_cube = "".join(sorted(str(cube)))
  cache[str_cube] += 1

for i in range(1,100000):
  cube = i**3
  str_cube = "".join(sorted(str(cube)))
  if cache[str_cube] == 5:
    print i, i**3
    sys.exit(0)
