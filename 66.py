from fractions import Fraction
from decimal import *

getcontext().prec = 100

def ContinuedFraction(D):
  last = [Fraction(Decimal(D).sqrt())]
  a = [int(D ** 0.5)]
  reciprocols = []

  i = 1
  while True:
    if last[i-1] - a[i-1] == 0:
      print D, a
    reciprocols.append(Fraction(1)/(last[i-1] - a[i-1]))
    a.append(int(reciprocols[i-1]))
    last.append(reciprocols[i-1])
    i = i + 1
    if a[-1] == 2 * a[0]:
      break
  return a

def Findxy(a):
  r = len(a) - 2
  a = a + a[1:] + a[1:]
  p = [a[0], a[0] * a[1] + 1]
  q = [1, a[1]]

  i = 2
  while i <= 2*r + 1:
    p.append(a[i] * p[i-1] + p[i-2])
    q.append(a[i] * q[i-1] + q[i-2])
    i = i + 1

  if r % 2 == 1:
    return p[r], q[r]
  else:
    return p[2*r+1], q[2*r+1]


best_x = 0
best_d = 0
for d in range(3, 1000):
  root = d ** 0.5
  if int(root) == root:
    continue
  continued_fraction = ContinuedFraction(d)
  r = len(continued_fraction) - 1
  x, y = Findxy(continued_fraction)
  if x > best_x:
    best_x = x
    best_d = d

print best_x, best_d


