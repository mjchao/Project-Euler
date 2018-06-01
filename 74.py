
factorial = [1 for _ in range(10)]
for i in range(1, 10):
  factorial[i] = factorial[i-1] * i


next_cache = [0 for _ in range(3000001)]

def ComputeNext(val):
  answer = 0
  for c in str(val):
    answer += factorial[int(c)]

  return answer

for i in range(1, 3000001):
  next_cache[i] = ComputeNext(i)

print ComputeNext(169)

cache = {}
def ChainLen(start_num):
  seen = set()
  seen.add(start_num)

  last = start_num
  length = 1
  while True:
    if len(seen) > 63:
      return 1000
    next_num = next_cache[last]
    if next_num not in seen:
      if next_num in cache:
        return length + cache[next_num]
      seen.add(next_num)
      length += 1
      last = next_num
    else:
      break

  cache[start_num] = length
  return length

print ChainLen(69)
print ChainLen(78)
print ChainLen(540)


answer = 0
for i in range(1, 1000000):
  chain_len = ChainLen(i)
  print i, chain_len
  if chain_len == 60:
    answer += 1

print "ANSWER:", answer


