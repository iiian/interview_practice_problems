from test_util import *

def longest_inc_subsequence(array):
  L = len(array)
  M = [1 for _ in range(L)]
  for i in range(L):
    for j in range(i):
      # the idea is that, if we assume M has the longest
      # subsequence for every previous element, then if we were
      # to add another element, we just need to take the max increase
      if array[j] < array[i]:
        M[i] = max(M[i], M[j] + 1)
  return max(M)

test_suite(
  test(4, Deferred(longest_inc_subsequence, [0, 2, 4, 6])),
  test(1, Deferred(longest_inc_subsequence, list(reversed([0, 2, 4, 6])))),
  test(4, Deferred(longest_inc_subsequence, [0, 2, 4, 6, 5, 4, 3, 2, 1])),
)