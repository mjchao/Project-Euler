from fractions import gcd

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

def Reduce(a,b,c):
  divisor = gcd(gcd(a,b),c)
  while divisor != 1:
    a /= divisor
    b /= divisor
    c /= divisor
    divisor = gcd(gcd(a,b),c)

  return (min(a,b), max(a,b), c)

N = 1500000
#N = 48
primes_list = sieve(N)
primes = primes_list

found = set()
counts = [0 for _ in range(N+1)]
prime_factors = [[] for _ in range(N+1)]
for p in primes:
  print "prime factorizing", p
  i = 1
  while True:
    num = p*i
    if num > N:
      break
    prime_factors[num].append(p)
    i += 1

prime_factors_dup = [[] for _ in range(N+1)]
for i in range(2, N+1):
  print "factorizing", i
  remainder = i
  for p in prime_factors[i]:
    while remainder % p == 0:
      prime_factors_dup[i].append(p)
      remainder /= p

checked_bs = set()
for i in range(2, N+1):
  if i % 10000 == 0:
    print "solving", i

  factors = prime_factors_dup[i]

  for bitset in range(2**len(factors)):
    m = 1
    n = 1
    for j in range(len(factors)):
      if bitset & (1 << j) == 0:
        m *= factors[j]
      else:
        n *= factors[j]
    b = 2*m*n
    if b in checked_bs:
      continue
    else:
      checked_bs.add(b)
    a = m*m - n*n
    c = m*m + n*n
    if a >= 3 and b >= 3 and c >= 3:
      if a*a + b*b == c*c:
        base_triple = Reduce(a,b,c)
        if base_triple not in found:
          found.add(base_triple)
          base_triple_sum = sum(base_triple)
          multiplier = 1
          while multiplier * base_triple_sum <= N:
            counts[multiplier * base_triple_sum] += 1
            multiplier += 1

answer = 0
for i in range(N+1):
  if counts[i] == 1:
    answer += 1

print answer



