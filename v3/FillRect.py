def fill(color, bitmap, start_point):
  point_q = [start_point]
  mask_color = bitmap[start_point]
  y_max, x_max = bitmap.shape
  while point_q:
    curr_point = point_q.pop()
    y_curr, x_curr = curr_point
    if bitmap[curr_point] == mask_color:
      bitmap[curr_point] = color
      if y_curr+1 < y_max:
        point_q.append((y_curr+1, x_curr))
      if y_curr-1 >= 0:
        point_q.append((y_curr-1, x_curr))
      if x_curr+1 < x_max:
        point_q.append((y_curr, x_curr+1))
      if x_curr >= 0:
        point_q.append((y_curr, x_curr-1))

import numpy as np

print('TEST #1')
bitmap = np.zeros(100).reshape(10,10)
fill(32, bitmap, (3, 6))
print(bitmap)
print('TEST #2')
bitmap = np.zeros(100).reshape(10,10)
for i in range(4):
  bitmap[i,6] = 1
for i in range(4):
  bitmap[4,6+i] = 1
fill(32, bitmap, (0, 9))
print(bitmap)