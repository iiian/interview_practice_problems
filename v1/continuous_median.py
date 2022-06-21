from test_util import *
from heap import MinHeap, MaxHeap

class ContinuousMedianManager:
  def __init__(self):
    self.left = MaxHeap([])
    self.right = MinHeap([])

  def add(self, value):
    if len(self.left) == len(self.right):
      self.left.insert(value)
    else:
      share = self.left.remove()
      self.right.insert(share)
      self.left.insert(value)

  def get_median(self):
    if len(self.left) > len(self.right):
      return self.left.peek_max()
    return (self.left.peek_max() + self.right.peek_min()) / 2

cmed = ContinuousMedianManager()
cmed.add(3)
test(
  3,
  Deferred(ContinuousMedianManager.get_median, cmed)
)
cmed.add(7)
test(
  5,
  Deferred(ContinuousMedianManager.get_median, cmed)
)
cmed.add(4)
test(
  7,
  Deferred(ContinuousMedianManager.get_median, cmed)
)