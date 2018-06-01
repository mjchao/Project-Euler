import collections

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

primes = sieve(10**8)
primes_set = set(primes)
MAX_N = 10**4

def PairWorks(p1, p2):
  #return IsPrime(int(str(p1) + str(p2))) and IsPrime(int(str(p2) + str(p1)))
  return int(str(p1) + str(p2)) in primes_set and int(str(p2) + str(p1)) in primes_set

cache = collections.defaultdict(set)
for i in range(MAX_N):
  for j in range(i+1, MAX_N):
    if PairWorks(primes[i], primes[j]):
      cache[primes[i]].add(primes[j])
      cache[primes[j]].add(primes[i])

print 3 in primes
print 7 in cache[3]
print 109 in cache[7] and 109 in cache[3]
print 673 in cache[109] and 673 in cache[7] and 673 in cache[3]

answers = []
for p1 in primes:
  for p2 in cache[p1]:
    for p3 in cache[p2]:
      if p3 not in cache[p1]:
        continue
      for p4 in cache[p3]:
        if p4 not in cache[p1] or p4 not in cache[p2]:
          continue
        for p5 in cache[p4]:
          if p5 not in cache[p1] or p5 not in cache[p2] or p5 not in cache[p3]:
            continue
          answers.append(p1 + p2 + p3 + p4 + p5)

print min(answers)


