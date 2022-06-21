from test_util import *

# Given a set of n items numbered from 1 up to n,
# each with a weight wi and a value vi, 
# along with a maximum weight capacity W, 
# maximize the sum of the values of the items in the
# knapsack so that the sum of the weights is less than 
# or equal to the knapsack's capacity.

def compute_knapsack_dp(w_max, items):
  # ks problem is solvable by considering how adding one more item to the items
  # set affects the output value.
  # it's actually a bit like the edit distance problem, where there's a matrix
  M = [ [ 0 for w in range(w_max+1) ] for i in range(len(items)+1) ]
  
  for i in range(1, len(items)+1):
    value = items[i-1].v
    weight = items[i-1].w
    for w in range(weight, w_max+1):
      M[i][w] = max(
        M[i-1][w],
        value + M[i-1][w-weight]
      )
  
  return M

# Implementation to the knapsack problem
def get_max_value(w_max, items):
  M = compute_knapsack_dp(w_max, items)
  return M[len(items)][w_max]

def get_max_value_items_subset(w_max, items):
  M = compute_knapsack_dp(w_max, items)
  items_subset = []
  i, w = len(items), w_max
  while i >= 1 and w >= 1:
    if M[i-1][w] == M[i][w]:
      i = i - 1
    if M[i-1][w] < M[i][w]:
      item = items[i-1]
      items_subset.append(item)
      w = w - item.w
      i = i - 1
    else: 
      break

  return items_subset



class I:
  def __init__(self, weight, value):
    self.w = weight
    self.v = value

  def __repr__(self):
    return f"{self.w}|{self.v}"

def test_suite(w_max, items):
  maximized_items_subset = get_max_value_items_subset(w_max, items)
  test(
    w_max,
    Deferred(
      sum, 
      [*map(lambda item: item.w, maximized_items_subset)]
    )
  )
  e_max_value = sum(map(lambda item: item.w, maximized_items_subset))
  test(
    e_max_value,
    Deferred(get_max_value, w_max, items)
  )

test_suite(7, [I(4, 10), I(1, 3), I(1, 4)])
test_suite(9, [I(4,10), I(1,3), I(1,4), I(3,2), I(2,7), I(2,9), I(1,2), I(2,6)])
test_are_eq(
  Deferred(get_max_value, 16, [I(4,10), I(1,3), I(1,4), I(3,2), I(2,7), I(2,9), I(1,2), I(2,6)]),
  Deferred(get_max_value, 17, [I(4,10), I(1,3), I(1,4), I(3,2), I(2,7), I(2,9), I(1,2), I(2,6)])
)
test_suite(3, [I(4, 10), I(1, 3), I(1, 4)])
test_suite(4, [I(4, 1), I(5, 2), I(1, 3)])
test_suite(4, [I(4, 10), I(1, 3), I(1, 4)])