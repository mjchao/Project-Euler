best_x2 = 0
best_d = 0
for d in xrange(1,1001):
#for d in xrange(1, 7):
  if int(d ** 0.5) ** 2 == d:
    continue
  found = False
  i = 0
  while True:
    i = i + 1
    s = i * i
    val = d * s + 1
    root = val ** 0.5
    if int(root) == root:
      if val > best_x2:
        best_x2 = val
        best_d = d
      print d, val
      found = True
      break

print best_d, best_x2
