import collections
from fractions import Fraction
import sys
import math
from decimal import *
getcontext().prec = 6

def sieve(n):
    """
    Generate the primes less than or equal to n using the sieve of
    Eratosthenes.
    """
    primes, sieve = [], [True] * (n + 1)
    for p in range(2, n + 1):
        if sieve[p]:
            primes.append(p)
            for i in range(p * p, n + 1, p):
                sieve[i] = False
    return primes

def IsPrime(n):
  if n % 2 == 0:
    return False
  for i in range(3,n,2):
    if i * i > n:
      break
    if n % i == 0:
      return False
  return True

MAX_N = 10**7
primes = sieve(MAX_N)

factors = [[] for _ in range(MAX_N)]
totient = [i for i in range(MAX_N)]
for p in primes:
  totient[p] = p - 1
  print p
  multiplier = 2
  while p*multiplier < MAX_N:
    totient[p*multiplier] = totient[p*multiplier] * (1 - float(1)/p)
    multiplier += 1

print int(round(totient[87109]))
print float(87109)/int(round(totient[87109]))

best = -1
best_ratio = 9999999
for i in range(2,MAX_N):
  if i % 1000 == 0:
    print i
  t = int(round(totient[i]))
  if sorted(str(t)) == sorted(str(i)):
    ratio = float(i)/t
    if ratio < best_ratio:
      best_ratio = ratio
      best = i

print best, best_ratio




