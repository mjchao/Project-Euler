import math
MAX_N = 1500000

squares = []

i = 1
while i * i <= MAX_N:
  squares.append(i*i)
  i += 1

squares_set = set(squares)


count = [0 for _ in range(MAX_N+1)]

"""
for c in range(MAX_N):
  for s in squares:
    b = s - c
    if c > b and c - b in squares:
      a = int(math.sqrt(c+b) * math.sqrt(c-b))
      if a >= 3 and b >= 3 and c >= 3:
        #print a, b, c
        if a + b + c <= MAX_N:
          count[a+b+c] += 1
"""

for c in range(3, MAX_N):
  print c
  for a in range(3, c):
    sq = (c+a) * (c-a)
    b = int(math.sqrt(sq))
    if b < a:
      break
    if b * b == sq and a >= 3 and b >= 3 and c >= 3:
      #print a, b, c
      if a + b + c <= MAX_N:
        count[a + b + c] += 1

answer = 0
for i in range(1, MAX_N+1):
  if count[i] == 1:
    answer += 1

print "ANSWER:", answer






