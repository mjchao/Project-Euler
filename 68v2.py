import itertools
import numpy as np
answers = []
target = 12
for x in itertools.permutations(range(1,7)):
  val0 = x[0] + x[1] + x[2]
  str0 = str(x[0]) + str(x[1]) + str(x[2])
  val1 = x[3] + x[2] + x[4]
  str1 = str(x[3]) + str(x[2]) + str(x[4])
  val2 = x[5] + x[4] + x[1]
  str2 = str(x[5]) + str(x[4]) + str(x[1])
  if val0 == target and val1 == target and val2 == target:
    answer_set = [str0, str1, str2]
    i = np.argmin([x[0], x[3], x[5]])
    answer_str = "".join(answer_set[i:] + answer_set[:i])
    answers.append(int(answer_str))

for x in set(answers):
  print x
print max(answers)


