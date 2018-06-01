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

def miller_rabin(n, k=10):
  if n == 2:
    return True
  if not n & 1:
    return False

  def check(a, s, d, n):
    x = pow(a, d, n)
    if x == 1:
      return True
    for i in xrange(s - 1):
      if x == n - 1:
        return True
      x = pow(x, 2, n)
    return x == n - 1

  s = 0
  d = n - 1

  while d % 2 == 0:
    d >>= 1
    s += 1

  for i in xrange(k):
    a = randrange(2, n - 1)
    if not check(a, s, d, n):
      return False
  return True


def is_prime(n):
  if n % 2 == 0:
    return False
  for i in range(3,n,2):
    if i * i > n:
      break
    if n % i == 0:
      return False
  return True


def GenSpiral(n):
  grid = [[0 for _ in range(n)] for _ in range(n)]
  center_row = n//2
  center_col = n//2

  grid[center_row][center_col] = 1
  next_num = 2
  curr_row = center_row
  curr_col = center_col + 1
  total_primes = 0
  for i in range(3, n+1, 2):
    # up
    for j in range(i - 2):
      grid[curr_row][curr_col] = next_num
      if next_num in primes:
        total_primes += 1
      next_num += 1
      curr_row -= 1

    # left
    for j in range(i - 1):
      grid[curr_row][curr_col] = next_num
      if next_num in primes:
        total_primes += 1
      next_num += 1
      curr_col -= 1

    # down
    for j in range(i - 1):
      grid[curr_row][curr_col] = next_num
      if next_num in primes:
        total_primes += 1
      next_num += 1
      curr_row += 1

    # right
    for j in range(i - 1):
      grid[curr_row][curr_col] = next_num
      if next_num in primes:
        total_primes += 1
      next_num += 1
      curr_col += 1

    # up again
    for j in range(1):
      grid[curr_row][curr_col] = next_num
      next_num += 1
      curr_row -= 1
    if next_num > 10**6:
      print "BAD"

    curr_col += 1
    curr_row += 1

  #for i in range(n):
    #print grid[i]

  primes_ne_diag = 0
  primes_nw_diag = 0

  curr_row = center_row
  curr_col = center_col
  for i in range(1,n//2+1):

    # ne
    if grid[curr_row-i][curr_col+i] in primes:
      primes_ne_diag += 1
    if grid[curr_row+i][curr_col-i] in primes:
      primes_ne_diag += 1

    # nw
    if grid[curr_row-i][curr_col-i] in primes:
      primes_nw_diag += 1
    if grid[curr_row+i][curr_col+i] in primes:
      primes_nw_diag += 1

  percentage = float(primes_ne_diag + primes_nw_diag)/(2*n - 1)
  return percentage


def GenSpiral2(n):
  total_primes = 0
  curr_num = 1
  for i in range(3,n+1,2):
    for j in range(4):
      curr_num += (i - 1)
      if miller_rabin( curr_num ):
        total_primes += 1

  return float(total_primes)/(2*n - 1)


for i in range(5, 100000, 2):
  percentage = GenSpiral2(i)
  print i, percentage
  if percentage < 0.1:
    break

