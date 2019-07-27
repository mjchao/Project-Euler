import math 

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

N = 50000000
N = 50
max_squared_prime = int(math.sqrt(N))
max_cubed_prime = int(N ** (1./3))
max_fourth_prime = int(N ** (1./4))

primes = sieve(max_squared_prime)
squares = [x*x for x in primes]
cubes = [x**3 for x in primes if x <= max_cubed_prime]
fourths = [x**4 for x in primes if x <= max_fourth_prime]

print len(squares), len(cubes), len(fourths)

answers = set()
for a in squares:
  for b in cubes:
    for c in fourths:
      test = a + b + c
      if test < N:
        answers.add(test)

print len(answers)
#print answers
# 1097343
