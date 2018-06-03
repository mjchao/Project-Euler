MIN_LEN = 50

for MAX_N in range(MIN_LEN+1, 1000):
  # end_with_red[i] is number of valid ways to fill length i ending with red
  end_with_red = [0]

  # end_with_black[i] is number of valid ways to fill length i ending with black
  end_with_black = [1]

  for i in range(1, MAX_N+1):
    end_with_red.append(0)
    end_with_black.append(0)

    # can add black to anything
    end_with_black[i] = end_with_black[i-1] + end_with_red[i-1]

    # can add one more red to anything ending with
    end_with_red[i] += end_with_red[i-1]

    # have to add at least 3 red squares to anything ending with black
    if i - MIN_LEN >= 0:
      end_with_red[i] += end_with_black[i-MIN_LEN]

  answer = end_with_red[MAX_N] + end_with_black[MAX_N]
  if answer > 1000000:
    print MAX_N
    break


