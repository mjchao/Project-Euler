from fractions import Fraction

N = 12

answer = 0
for i in range(2, N+1):
  num = 0
  for j in range(1,i):
    test = Fraction(j, i)
    if test.denominator == i:
      num += 1
      answer += 1
  print i, num

print answer
