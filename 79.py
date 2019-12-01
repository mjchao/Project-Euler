passcodes = []
with open("79.txt") as f:
  for line in f:
    passcodes.append(line.strip())

def isSubsequence(n, passcode):
  i = 0
  for c in passcode:
    matched = False
    while i < len(n):
      if c == n[i]:
        matched = True
        i += 1
        break
      else:
        i += 1
    if not matched:
      return False
  return True

def trim(s):
  removed_anything = True
  while (removed_anything):
    removed_anything = False
    for i in range(len(s)):
      new_candidate = s[0:i] + s[i+1:]
      new_candidate_works = True
      for p in passcodes:
        if not isSubsequence(new_candidate, p):
          new_candidate_works = False
          break
      if new_candidate_works:
        s = new_candidate
        removed_anything = True
        print new_candidate
        break
  return s

s = "".join(passcodes)
s = trim(s)
print s
# 8731629809

test = "73162909"
for i in range(len(test)):
  new_candiate = test[0:i] + "8" + test[i:]
  new_candidate_works = True
  for p in passcodes:
    if not isSubsequence(new_candiate, p):
      new_candidate_works = False
  if new_candidate_works:
    print new_candiate
    break


#731628909
test = "7316280"
for i in range(len(test)):
  new_candiate = test[0:i] + "9" + test[i:]
  new_candidate_works = True
  for p in passcodes:
    if not isSubsequence(new_candiate, p):
      new_candidate_works = False
  if new_candidate_works:
    print new_candiate
    break

#73162890


