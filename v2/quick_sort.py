def quick_sort(array):
  def _quicksort(lo, hi):
    if hi <= lo:
      return
    if hi - lo < 2:
      if array[hi] < array[lo]:
        array[hi], array[lo] = array[lo], array[hi]
      return
    def _pivot(p, r):
      l = p+1
      pivot = array[p]
      while l <= r:
        if array[l] < pivot:
          l += 1
        elif pivot <= array[r]:
          r -= 1
        elif array[r] < pivot < array[l]:
          array[r], array[l] = array[l], array[r]
      array[r], array[p] = array[p], array[r]
      return r
    
    p = _pivot(lo, hi)
    _quicksort(lo, p-1)
    _quicksort(p+1, hi)

  _quicksort(0, len(array)-1)
  return array

from testing import test_case, TestSuite
from random import shuffle

suite = TestSuite()
for i in range(0, 1000):
    def create_test(i):
        def test():
            array = list(range(i))
            input = array.copy()
            shuffle(input)
            return test_case(
                f"it should sort the array ({i+1})",
                quick_sort(input),
                array
            )
        return test
    suite.add_test(create_test(i))

suite.run_all()