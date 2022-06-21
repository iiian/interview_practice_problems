from typing import List
from test_util import *

class Disk:
  def __init__(self, w, h, d):
    self.w = w
    self.h = h
    self.d = d

# sort the disks, s.t. as the order ascends,
# the width/height of the former encompasses that of the latter.
# additionally, depth former >= depth latter.
def stack_disks(disks: List[Disk]):
  disks.sort(key=lambda disk: disk.d)
  # this solution is a bit like a knapsack or longest inc subsequence problem.
  # we'll build a DPM, where the dimensions grow based on:
  # (horiz) 
  # (vert)
  L = len(disks)
  for i in range(L):
    for j in range(i):
      if disks[i].w >= disks[j].w and disks[i].h >= disks[j].h:
        swap(disks, i, j)

  return disks

def swap(disks, i, j):
  disks[i],disks[j]=disks[j],disks[i]

disks = [Disk(4,4,4),Disk(3,3,3),Disk(2,2,2),Disk(1,1,1),Disk(0,0,0)]
stack_disks(disks)

disks = [Disk(0,0,0),Disk(1,1,1),Disk(2,2,2),Disk(3,3,3),Disk(4,4,4)]
stack_disks(disks)