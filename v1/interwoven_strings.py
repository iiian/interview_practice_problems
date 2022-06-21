from test_util import *

def interwoven_strings(a, b, c):
  La, Lb, Lc = len(a), len(b), len(c)
  cache = {}
  def recurse(i,j):
    if (i+j) not in cache:
      if i + j == Lc: 
        cache[i+j] = False
        return False
      if i == La: 
        cache[i+j] = b[j:] == c[i+j:]
        return b[j:] == c[i+j:]
      if j == Lb: 
        cache[i+j] = a[i:] == c[i+j:]
        return a[i:] == c[i+j:]
    cache[i+j] = (
      (c[i+j] == a[i] and recurse(i+1,j)) or
      (c[j+i] == b[j] and recurse(i,j+1))
    )
    return cache[i+j]

  return recurse(0,0)


test(
  True,
  Deferred(interwoven_strings,
    'this should create some problems',
    'really just for me quite hairy',
    'this really just for me should create some quite hairyproblems'
  )
)

test(
  True,
  Deferred(interwoven_strings, 'inter', 'woven', 'interwoven')
)
test(
  True,
  Deferred(interwoven_strings, 'inter', 'woven', 'iwonterven')
)
test(
  True,
  Deferred(interwoven_strings, 'inter', 'woven', 'iwontvener')
)