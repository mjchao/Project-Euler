import math
N = 1500000
#N = 48

squares = [x*x for x in range(N//2)]
squares_set = set(squares)
ways_to_form = [0 for _ in range(N+1)]


def SatisfiesTriangleInequality(a, b, c):
  return a >=3 and b >= 3 and c >= 3 and a + b > c

for b in range(4, len(squares)):
  if b % 1000 == 0:
    print b
  b2 = squares[b]
  i = 1
  while i*i <= b2:
    if b2 % i == 0:
      j = b2 / i
      # b^2 = i * j
      # solve c - a = i     and      c + a = j
      if (i+j) % 2 == 0:
        c = (i + j)/2
        a = (j - i)/2
        if a <= b and a + b + c <= N and SatisfiesTriangleInequality(a, b, c):
          #print a, b, c, i, j
          ways_to_form[a + b + c] += 1
    i += 1

answer = 0
for i in range(N+1):
  if ways_to_form[i] == 1:
    answer += 1

print answer

