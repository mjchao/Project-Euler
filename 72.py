import collections
import itertools
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

MAX_N = 1000000
#MAX_N = 12
primes = sieve(MAX_N+1)

prime_factors = [[] for _ in range(MAX_N+1)]
for p in primes:
  i = 1
  while True:
    num = p*i
    if num > MAX_N:
      break
    prime_factors[num].append(p)
    i += 1

answer = 0
num_with_prime_factor = [0 for _ in range(MAX_N+1)]
for i in range(2,MAX_N+1):
  if i % 1000 == 0:
    print i
  tmp = set()
  num_common = 0
  total = 0
  for j in range(0,len(prime_factors[i])+1):
    if j % 2 == 1:
      sign = 1
    else:
      sign = -1

    for factor_choices in itertools.combinations(prime_factors[i], j):
      prod = 1
      for factor in factor_choices:
        prod *= factor
      total += (sign * (i // prod))
  answer += -1*total

print answer


