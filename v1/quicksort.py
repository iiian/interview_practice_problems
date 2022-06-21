from test_util import *

def quick_sort(array):
  def swp(a,b):
    array[a],array[b]=array[b],array[a]

  def partition(p, r):
    l = p + 1
    while l <= r:
      if array[l] < array[p]:
        l += 1
      if array[p] <= array[r]:
        r -= 1
      if l > r: break
      if array[r] < array[p] <= array[l]:
        swp(l, r)
        r -= 1
        l += 1
    swp(p, r)
    return r

  def run(l, r):
    if l >= r: return
    p = partition(l, r)
    run(l, p-1)
    run(p+1, r)
  
  run(0, len(array)-1)
  return array

sorte = quick_sort([3,8,2,1,7,4, 19,15, 2, 0])
print('check)')
