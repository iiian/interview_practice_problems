import unittest

def min_hops(arr):
  curr = 0
  total_hops = 0
  L = len(arr)
  while curr+1 < L:
    leap_range = arr[curr]
    curr_acc_lim = min(curr + leap_range + 1, L)
    best_step, best_step_idx = 0, -1
    for i in range(curr+1, curr_acc_lim):
      if best_step < arr[i]:
        best_step, best_step_idx = arr[i], i
    curr = best_step_idx
    total_hops += 1

  return total_hops+1

class TestCases(unittest.TestCase):
  def test1(self):
    hops = min_hops([1,1])
    self.assertEqual(hops, 2, f'{hops} != 2')

  def test2(self):
    hops = min_hops([3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3])
    self.assertEqual(hops, 5, f'{hops} != 5')

  def test3(self):
    hops = min_hops([1,1,1,1,1,1,1])
    self.assertEqual(hops, 7, f'{hops} != 7')

if __name__ == '__main__':
  unittest.main()