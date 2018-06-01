WIDTH = 2
HEIGHT = 9
MAX = WIDTH * HEIGHT

done = False
dp = {}
def Search(curr_state):
  if curr_state in dp:
    return curr_state

  for i in range(MAX):
    if curr_state & (1 << i) == 0:
      answer = 0
      # 90 degree piece
      if i % WIDTH < WIDTH - 1 and i // WIDTH < HEIGHT - 1:

        if (curr_state & ((1 << i) + (1 << (i+1)) + (1 << (i+WIDTH))) == 0 ):
          next_state_1 = curr_state
          next_state_1 = next_state_1 | (1 << i)
          next_state_1 = next_state_1 | (1 << (i+1))
          next_state_1 = next_state_1 | (1 << (i + WIDTH))
          answer += Search(next_state_1)

        if (curr_state & ((1 << i) + (1 << (i+1)) + (1 << (i+WIDTH+1))) == 0):
          next_state_2 = curr_state
          next_state_2 = next_state_2 | (1 << i)
          next_state_2 = next_state_2 | (1 << (i+1))
          next_state_2 = next_state_2 | (1 << (i + WIDTH + 1))
          answer += Search(next_state_2)

        if (curr_state & ((1 << i) + (1 << (i+WIDTH)) + (1 << (i+WIDTH+1))) == 0):
          next_state_3 = curr_state
          next_state_3 = next_state_3 | (1 << i)
          next_state_3 = next_state_3 | (1 << (i + WIDTH))
          next_state_3 = next_state_3 | (1 << (i + WIDTH + 1))
          answer += Search(next_state_3)

        if (curr_state & ((1 << (i+1)) + (1 << (i+WIDTH)) + (1 << (i+WIDTH+1))) == 0):
          next_state_4 = curr_state
          next_state_4 = next_state_4 | (1 << (i + 1))
          next_state_4 = next_state_4 | (1 << (i + WIDTH))
          next_state_4 = next_state_4 | (1 << (i + WIDTH + 1))
          answer += Search(next_state_4)

      # 3 squares down
      if i // WIDTH < HEIGHT - 2:
        if (curr_state & ((1 << i) + (1 << (i+WIDTH)) + (1 << (i+WIDTH+WIDTH))) == 0):
          next_state_5 = curr_state
          next_state_5 = next_state_5 | (1 << i)
          next_state_5 = next_state_5 | (1 << (i + WIDTH))
          next_state_5 = next_state_5 | (1 << (i + WIDTH + WIDTH))
          answer += Search(next_state_5)

      # 3 squares right
      if i % WIDTH < WIDTH - 2:
        if (curr_state & ((1 << i) + (1 << (i+1)) + (1 << (i+2))) == 0):
          next_state_6 = curr_state
          next_state_6 = next_state_6 | (1 << i)
          next_state_6 = next_state_6 | (1 << (i + 1))
          next_state_6 = next_state_6 | (1 << (i + 2))
          answer += Search(next_state_6)

      dp[curr_state] = answer
      return answer
  return 1

print Search(0)
print dp


for i in range(MAX):
  print i // WIDTH, i % WIDTH
