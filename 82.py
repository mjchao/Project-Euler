INF = 999999

ROWS = 80
COLS = 80
FILENAME = "82.txt"

# sample case
ROWS = 5
COLS = 5
FILENAME = "82_sample.txt"

grid = [[0 for _ in range(ROWS)] for _ in range(COLS)]

with open(FILENAME) as f:
  for i, line in enumerate(f):
    numbers = line.split(",")
    for j, num in enumerate(numbers):
      grid[i][j] = int(num)


dRow = [0, 1, -1]
dCol = [1, 0, 0]
def dijkstra(start_row):
  min_dist = [[INF for _ in range(ROWS)] for _ in range(COLS)]
  visited = [[False for _ in range(ROWS)] for _ in range(COLS)]
  min_dist[start_row][0] = grid[start_row][0]

  max_iters = (ROWS + 1) * (COLS + 1)
  for dijkstra_iter in range(max_iters):
    visit_row = -1
    visit_col = -1
    visit_dist = INF
    for row in range(ROWS):
      for col in range(COLS):
        if not visited[row][col] and min_dist[row][col] < visit_dist:
          visit_dist = min_dist[row][col]
          visit_row = row
          visit_col = col

    visited[visit_row][visit_col] = True
    if visit_row == -1:
      raise ValueError("Error occurred in dijkstra algo")

    for i in range(len(dRow)):
      neighbor_row = visit_row + dRow[i]
      neighbor_col = visit_col + dCol[i]
      if (0 <= neighbor_row and neighbor_row < ROWS and
          0 <= neighbor_col and neighbor_col < COLS):
        neighbor_dist = visit_dist + grid[neighbor_row][neighbor_col]
        if neighbor_dist < min_dist[neighbor_row][neighbor_col]:
          if visited[neighbor_row][neighbor_col]:
            raise ValueError("Error in dijkstra visited set")
          min_dist[neighbor_row][neighbor_col] = neighbor_dist

    if all(visited[row][COLS-1] for row in range(ROWS)):
      return min(min_dist[row][COLS-1] for row in range(ROWS))

  raise ValueError("Dijkstra did not terminate in max_iters")

answer = INF
for row in range(ROWS):
  answer = min(answer, dijkstra(row))

print "ANSWER", answer

