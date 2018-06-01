import itertools
import numpy as np
answers = []
for x in itertools.permutations(range(1,11)):
  val0 = x[0] + x[1] + x[2]
  str0 = str(x[0]) + str(x[1]) + str(x[2])
  val1 = x[3] + x[2] + x[4]
  str1 = str(x[3]) + str(x[2]) + str(x[4])
  val2 = x[5] + x[4] + x[6]
  str2 = str(x[5]) + str(x[4]) + str(x[6])
  val3 = x[7] + x[6] + x[8]
  str3 = str(x[7]) + str(x[6]) + str(x[8])
  val4 = x[9] + x[8] + x[1]
  str4 = str(x[9]) + str(x[8]) + str(x[1])
  if val0 == val1 and val0 == val2 and val0 == val3 and val0 == val4:
    answer_set = [str0, str1, str2, str3, str4]
    i = np.argmin([x[0], x[3], x[5], x[7], x[9]])
    answer_str = "".join(answer_set[i:] + answer_set[:i])
    if len(answer_str) == 16:
      answers.append(int(answer_str))

print max(answers)


