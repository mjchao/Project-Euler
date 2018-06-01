import sys

answer = 0
for i in range(1, 100):
  for exp in range(1, 100):
    if len(str(i ** exp)) == exp:
      answer += 1

print answer

