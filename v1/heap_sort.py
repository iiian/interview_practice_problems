from test_util import *

def heap_sort(array):
  L = len(array)

  def swap(a,b):
    array[a],array[b]=array[b],array[a]

  def max_heapify(lo, hi):
    for i in reversed(range(lo, hi)):
      sift_down(i, hi)

  def sift_down(i, hi):
    while 2*i+1 < hi:
      cli = 2*i+1
      cri = 2*i+2
      t = array[i]
      cl = array[cli] if cli < hi else -float('inf')
      cr = array[cri] if cri < hi else -float('inf')
      if cl > t and cl >= cr:
        swap(i, cli)
        i = cli
      elif cr > t and cr >= cl:
        swap(i, cri)
        i = cri
      else: break

  max_heapify(0, L)
  for i in range(L):
    swap(0, L-i-1)
    sift_down(0, L-i-1)

  return array

result = ([3,2,8,4,3,7,1,9,4,7,1])

test_suite(
  test(
    [1,1,2,3,3,4,4,7,7,8,9],
    Deferred(heap_sort, [3,2,8,4,3,7,1,9,4,7,1])
  ),
  test(
    [1,2,3,4,5],
    Deferred(heap_sort, [5,4,3,2,1])
  )
)

