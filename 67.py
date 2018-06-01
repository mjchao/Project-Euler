max_sum = [[-1 for _ in range(110)] for _ in range(110)]
max_sum[1][1] = 59

with open("67.txt") as f:
  f.readline()
  for i in range(2,101):
    nums = [int(x) for x in f.readline().split()]
    for j in range(1,i+1):
      if j == 1:
        max_sum[i][j] = max_sum[i-1][j] + nums[j-1]
      elif j == i:
        max_sum[i][j] = max_sum[i-1][j-1] + nums[j-1]
      else:
        max_sum[i][j] = max(max_sum[i-1][j-1], max_sum[i-1][j]) + nums[j-1]

answer = -1
for i in range(1, 101):
  answer = max(answer, max_sum[100][i])

print answer



