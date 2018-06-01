from fractions import Fraction
MAX_N = 1000000

answer = None
best_diff = Fraction(99999)
ref = Fraction(3, 7)
for i in range(MAX_N-1,MAX_N-1000,-1):
  if i % 100 == 0:
    print i
  start_num = 3*i
  start_denom = 7*i
  for j in range(start_num-1,0,-1):
    test = Fraction(j, start_denom)
    if test.denominator <= MAX_N:
      diff = (ref - test)
      if 0 <= diff and diff < best_diff:
        best_diff = diff
        answer = test
      break

print answer

