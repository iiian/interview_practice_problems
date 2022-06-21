from test_util import *

# validate heap invariant
def check_heap_invariant(heap):
  print("TEST:")
  for i in range(len(heap.items) // 2):
    cl = 2*i + 1
    cr = 2*i + 2
    ei = heap.items[i]
    el = heap.items[cl] if cl < len(heap.items) else float('inf')
    er = heap.items[cr] if cr < len(heap.items) else float('inf')
    if not assert_lt(ei, el) or not assert_lt(ei, er):
      return
  passed("heap invariant validated")

class MinHeap:
  def __init__(self, items):
    self.items = items
    self.__heapify()

  def __len__(self):
    return len(self.items)

  def __heapify(self):
    for i in reversed(range(len(self.items) // 2)):
      self.__sift_down(i)

  def __sift_up(self, pi):
    while True:
      i = pi
      pi = i // 2
      ei, ep = self.items[i], self.items[pi]
      if i == pi or ei >= ep:
        break
      self.__swap(i, pi)

  def insert(self, value): 
    self.items.append(value)
    self.__sift_up(len(self.items) - 1)

  def __sift_down(self, i = 0):
    while True:
      cl = 2*i + 1
      cr = 2*i + 2
      ei = self.items[i]
      el = self.items[cl] if cl < len(self.items) else float('inf')
      er = self.items[cr] if cr < len(self.items) else float('inf')
      if ei <= el and ei <= er: break
      if el < ei and el <= er:
        self.__swap(i, cl)
        i = cl
      elif er < ei and er < el:
        self.__swap(i, cr)
        i = cr

  def __swap(self, a, b):
    self.items[a], self.items[b] = self.items[b], self.items[a]

  def remove(self):
    if len(self.items) == 0:
      return None
    l_i = len(self.items) - 1
    self.items[0], self.items[l_i] = self.items[l_i], self.items[0]
    value = self.items.pop()
    self.__sift_down()
    return value
  
  def peek_min(self):
    return self.items[0]

class MaxHeap:
  def __init__(self, items):
    self.items = items
    self.__heapify()

  def __len__(self):
    return len(self.items)

  def __heapify(self):
    for i in reversed(range(len(self.items) // 2)):
      self.__sift_down(i)

  def __sift_up(self, pi):
    while True:
      i = pi
      pi = i // 2
      ei, ep = self.items[i], self.items[pi]
      if i == pi or ei <= ep:
        break
      self.__swap(i, pi)

  def insert(self, value): 
    self.items.append(value)
    self.__sift_up(len(self.items) - 1)

  def __sift_down(self, i = 0):
    if len(self) == 0:
      return
    while True:
      cl = 2*i + 1
      cr = 2*i + 2
      ei = self.items[i]
      el = self.items[cl] if cl < len(self.items) else float('inf')
      er = self.items[cr] if cr < len(self.items) else float('inf')
      if ei >= el and ei >= er: break
      if el > ei and el >= er:
        self.__swap(i, cl)
        i = cl
      elif er > ei and er > el:
        self.__swap(i, cr)
        i = cr

  def __swap(self, a, b):
    self.items[a], self.items[b] = self.items[b], self.items[a]

  def remove(self):
    if len(self.items) == 0:
      return None
    l_i = len(self.items) - 1
    self.items[0], self.items[l_i] = self.items[l_i], self.items[0]
    value = self.items.pop()
    self.__sift_down()
    return value
  
  def peek_max(self):
    return self.items[0]


heap = MinHeap([2, 6, 3, 4, 8, 30, 15,2 ,1, 9, 28, 4, 5, 24, 1, 12, 25])
check_heap_invariant(heap)
test(
  1,
  Deferred(MinHeap.peek_min, heap)
)
heap.insert(0)
test(
  0,
  Deferred(MinHeap.peek_min, heap)
)
test(
  0,
  Deferred(MinHeap.remove, heap)
)
test(
  1,
  Deferred(MinHeap.peek_min, heap)
)
heap.remove()
check_heap_invariant(heap)
heap.remove()
check_heap_invariant(heap)
heap.remove()
check_heap_invariant(heap)
test(
  2,
  Deferred(MinHeap.peek_min, heap)
)
check_heap_invariant(heap)
heap.insert(3000)
check_heap_invariant(heap)
heap.insert(30)
check_heap_invariant(heap)
heap.insert(30)
check_heap_invariant(heap)
heap.insert(30)
check_heap_invariant(heap)
heap.insert(30)
check_heap_invariant(heap)
heap.insert(30)
check_heap_invariant(heap)
heap.insert(30)
check_heap_invariant(heap)
heap.insert(30)
check_heap_invariant(heap)
heap.insert(30)
check_heap_invariant(heap)
heap.insert(30)
check_heap_invariant(heap)
heap.insert(30)
check_heap_invariant(heap)
heap.insert(30)
check_heap_invariant(heap)
heap.insert(30)
check_heap_invariant(heap)