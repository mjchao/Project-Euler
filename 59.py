import itertools
chars = [chr(c) for c in range(ord('a'), ord('z') + 1)]
with open("59.txt") as f:
  inputs = f.readline().rstrip("\n").split(",")
  inputs = [chr(int(x)) for x in inputs]

def decode(key):
  return "".join([chr(ord(inputs[i]) ^ ord(key[i%3])) for i in range(len(inputs))])

"""
for key in itertools.combinations_with_replacement(chars, 3):
  print key, decode(key)
  break
"""
solution = decode(["g", "o", "d"])
print sum([ord(x) for x in solution])
