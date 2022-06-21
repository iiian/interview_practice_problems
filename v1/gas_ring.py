from test_util import *

def gas_ring(refills, distances):
  total_deficit = 0
  leg_deficit = 0
  leg_start = 0
  L = len(refills)
  for i in range(L):
    # the going from i to i+1
    # is representable by:
    # (1) refilling @ i, (2) the distance to i+1, stored at distances[i].
    current_cost = refills[i] - distances[i]
    leg_deficit += current_cost
    # there is a total_deficit that has run since i=0, which does not reset
    total_deficit += current_cost
    # if we hit a leg of the trek where we need more fuel than we have
    if leg_deficit < 0:
      leg_start = i+1 % L
      leg_deficit = 0

  # we have computed the total ring energy value in traversing the entire array and
  # summing the diff between refills & distances. If the sum total is less than zero,
  # then that would imply that there would necessarily need to be an external amount
  # of energy injected into the vehicle to manage even a single rotation around the ring.
  # however, if it is == 0 or > 0, then the vehicle could traverse the ring indefinitely,
  # as the energy is either conserved or perpetually increasing.
  if total_deficit < 0:
    return -1
  
  # now, leg_start would be the last place where we had to reset our deficit assumptions.
  # consequently, it is then also the place where the max amount of energy can be collected,
  # as to overtake all of the most baren legs of the trip that we have previously encountered.
  # therefore, it is minimum place (although not necessarily the only place) from which the
  # entire ring is traversible.
  return leg_start

test_suite(
  # you cannot traverse a ring with length, but no fuel.
  test(
    -1,
    Deferred(gas_ring, [0,0,0,0,0], [1,1,1,1,1])
  ),
  # you can traverse a ring with no length.
  test(
    0,
    Deferred(gas_ring, [0,0,0,0,0], [0,0,0,0,0])
  ),
  # you can traverse a ring with perfect energy conservation.
  test(
    1,
    Deferred(gas_ring, [1,2,3,4,5], [5,1,2,3,4])
  ),
  # you can traverse a ring with perfect energy conservation.
  test(
    4,
    Deferred(gas_ring, [1,2,3,4,5], [2,3,4,5,1])
  ),
  # you can traverse a ring with net positive energy gain.
  test(
    2,
    Deferred(gas_ring, [0,0,6,0,0],[1,1,1,1,1])
  ),
)