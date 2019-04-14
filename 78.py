import collections
cache = {}
cache[0] = 1
cache[1] = 1

MOD = 1000000


sum_cache = {}
def cumulative_sum(begin, end):
  pass



def p(n):
  if n in cache:
    return cache[n]

  answer = 0
  for k in range(1,n+1):
    tmp1 = k * (3*k - 1) / 2
    tmp2 = k * (3*k + 1) / 2
    if 1 <= tmp1 and tmp1 <= n:
      answer += ((-1) ** (k+1)) * (p(n - tmp1))
      answer %= MOD
    if 1 <= tmp2 and tmp2 <= n:
      answer += ((-1) ** (k+1)) * (p(n - tmp2))
      answer %= MOD
  cache[n] = (answer % MOD)
  return answer

for i in range(10000):
  if p(i) % 1000 == 0:
    print i, p(i)
