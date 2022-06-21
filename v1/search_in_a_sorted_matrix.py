from test_util import *

def get_index(value, matrix):
  if len(matrix) == 0:
    return None
  M, N = len(matrix), len(matrix[0])
  m, n = 0, N - 1

  while 0 <= m < M and 0 <= n <= N and matrix[m][n] != value:
    if matrix[m][n] < value:
      m += 1
    else:
      n -= 1

  if 0 <= m < M and 0 <= n <= N:
    return (m, n)
  else:
    return None

test(
  (1, 3),
  Deferred(get_index, 7, [
    [0, 0, 3, 6],
    [1, 1, 3, 7],
    [2, 3, 4, 8],
    [5, 5, 5, 9],
  ])
)
test(
  (3, 2),
  Deferred(get_index, 19, [
    [0, 0, 2, 6],
    [1, 3, 4, 7],
    [5, 8, 9, 20],
    [10, 15, 19, 21],
  ])
)
test(
  None,
  Deferred(get_index, 32, [
    [0, 0, 2, 6],
    [1, 3, 4, 7],
    [5, 8, 9, 20],
    [10, 15, 19, 21],
  ])
)