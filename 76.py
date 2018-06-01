num_ways = {}

# number of ways to sum to n using numbers that are at most
# m
def NumWays(n, m):
#  print n, m
  if (n, m) in num_ways:
    return num_ways[(n,m)]

  if n == 0 and m == 0:
    return 1
  if m == 0:
    return 0
  if m > n:
    return NumWays(n,n)
  if m == 1:
    return 1

  answer = 0
  for i in range(1,m+1):
    answer += NumWays(n - i, i)
  num_ways[(n,m)] = answer
  return answer

print NumWays(100,99)
#print num_ways
