from test_util import *

def get_edit_distance(str_a, str_b):
  M = [
    [0 for a in range(len(str_a) + 1)]
    for b in range(len(str_b) + 1)
  ]
  for b in range(1, len(str_b) + 1):
    for a in range(1, len(str_a) + 1):
      cost = 0 if str_a[a-1] == str_b[b-1] else 1
      M[b][a] = min(
        cost + M[b-1][a-1],
        1 + M[b-1][a],
        1 + M[b][a-1]
      )

  return M[b][a]

test(3, Deferred(get_edit_distance, "cat", "dog"))
test(1, Deferred(get_edit_distance, "dot", "dog"))
test(4, Deferred(get_edit_distance, "cattle", "cadence"))
test(0, Deferred(get_edit_distance, "tree", "tree"))
test(1, Deferred(get_edit_distance, "tree", "tre"))
test(5, Deferred(get_edit_distance, "dimensions", "dementia"))