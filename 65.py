from fractions import Fraction

vals = [2]
for i in range(1,34):
  vals.append(1)
  vals.append(2*i)
  vals.append(1)

print vals[:5]

def Answer(n):
  answer = Fraction(vals[n])
  for i in range(n-1,-1,-1):
    answer = Fraction(1) / answer + vals[i]
  return answer

print sum([int(c) for c in str(Answer(99).numerator)])

