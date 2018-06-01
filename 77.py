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
primes_set = set(primes)
MAX_N = 10**4

dp = collections.defaultdict(lambda: collections.defaultdict(int))

# 1 way to make 2 with primes up to and including index 0
dp[0][0] = 1

i = 1
run = True
while run:
  i += 1
  for j in range(len(primes)):
    p = primes[j]
    if p > i:
      for k in range(j, len(primes)):
        dp[i][k] = dp[i][j-1]
      if i % 100 == 0:
        print i, dp[i][j-1]
      break
    if i - p == 0:
      dp[i][j] = dp[i][j-1] + 1
    else:
      dp[i][j] = dp[i][j-1] + dp[i - p][j]

    if dp[i][j] > 5000:
      print i, dp[i][j]
      run = False
      break

print dp[10][3]
print dp[3][3]


