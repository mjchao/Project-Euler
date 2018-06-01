from decimal import *
import sys

getcontext().prec = 100

def GetPeriod(n):
  m = int(n ** 0.5)
  x = 1
  y = m
  period = []
  while True:
    x = (n - y * y) / x
    period.append((m+y)/x)
    y = m - (m + y) % x
    if x <= 1:
      break
  return len(period)



answer = 0
for i in range(1, 10001):
#for i in range(1, 14):
  if int(i ** 0.5) ** 2 == i:
    continue
  period = GetPeriod(i)
  print i, period
  if period % 2 == 1:
    answer += 1

print answer

