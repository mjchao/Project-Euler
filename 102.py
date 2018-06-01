def CrossProduct(vec1, vec2):
  product = vec1[0] * vec2[1] - vec1[1] * vec2[0]
  if product > 0:
    return 1
  elif product == 0:
    return 0
  else:
    return -1

def OriginInTriangle( points ):
  centroid_x = (points[0][0] + points[1][0] + points[2][0])/3.0
  centroid_y = (points[0][1] + points[1][1] + points[2][1])/3.0

  vec_side1 = (points[0][0] - points[1][0], points[0][1] - points[1][1])
  vec_side2 = (points[1][0] - points[2][0], points[1][1] - points[2][1])
  vec_side3 = (points[2][0] - points[0][0], points[2][1] - points[0][1])

  side1_ok = (
      CrossProduct((centroid_x - points[0][0], centroid_y - points[0][1]), vec_side1) ==
        CrossProduct((0 - points[0][0], 0 - points[0][1]), vec_side1))

  side2_ok = (
      CrossProduct((centroid_x - points[1][0], centroid_y - points[1][1]), vec_side2) ==
        CrossProduct((0 - points[1][0], 0 - points[1][1]), vec_side2))

  side3_ok = (
      CrossProduct((centroid_x - points[2][0], centroid_y - points[2][1]), vec_side3) ==
        CrossProduct((0 - points[2][0], 0 - points[2][1]), vec_side3))

  return side1_ok and side2_ok and side3_ok

answer = 0

with open("102.txt") as f:
  for line in f:
    points = [float(x) for x in line.split(",")]
    triangle = [(points[0], points[1]), (points[2], points[3]), (points[4], points[5])]
    if OriginInTriangle(triangle):
      answer += 1

print answer


print OriginInTriangle([(-340,495), (-153,-910),(835,-947)])
print OriginInTriangle([(-175,41), (-421, -714), (574, -645)])
print OriginInTriangle([(1, 0), (0, 0), (0, 1)])



