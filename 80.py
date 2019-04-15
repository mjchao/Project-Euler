
def SqrtExpansion(n):
  n_str = str(n)
  if len(n_str) % 2 == 1:
    n_str = "0" + n_str
  n_str += ("0" * 200)

  root = 0
  remainder = 0
  for i in range(len(n_str)/2):
    current_value = remainder * 100 + int(n_str[2*i:2*(i+1)])
    next_expansion_digit = 0
    test = 0
    for j in range(10):
      tmp = j * (20 * root + j)
      if tmp > current_value:
        break
      else:
        next_expansion_digit = j
        test = tmp

    root = root * 10 + next_expansion_digit
    remainder = current_value - test
  return root

perfect_squares = {x*x for x in range(11)}
answer = 0
for i in range(1, 101):
  print "Iter ", i
  if i in perfect_squares:
    continue
  answer += sum(int(x) for x in str(SqrtExpansion(i))[:100])
print answer

