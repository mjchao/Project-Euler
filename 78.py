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

primes = sieve(10**3)
primes = range(1,10**4+1)

nways = [0, 0, 1]
dp = collections.defaultdict(lambda: collections.defaultdict(int))

# 1 way to make 2 with primes up to and including index 0
dp[0][0] = 1
for a in range(len(primes)):
  dp[0][a] = 1
  dp[1][a] = 1

i = 1
run = True
while run:
  i += 1
  for j in range(len(primes)):
    p = primes[j]
    if p > i:
      for k in range(j, len(primes)):
        dp[i][k] = dp[i][j-1]
      if i % 1000 == 0:
        print i
      break
    if i - p == 0:
      dp[i][j] = dp[i][j-1] + 1
    else:
      dp[i][j] = dp[i][j-1] + dp[i - p][j]

  if dp[i][i] % 1000000 == 0:
    print i, dp[i][i]
    run = False
    break

