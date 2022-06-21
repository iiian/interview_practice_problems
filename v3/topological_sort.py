from collections import defaultdict
from typing import List
import unittest


def toposort(vertices):
  # O(v) time, O(v) space
  nodes = set([
    f(v) for v in vertices 
    for f in (lambda x: x[0], lambda x: x[1])
  ])
  # O(n*v) time, O(v) space
  parent_map = {
    (node): { src for src, n in vertices if n == node }
    for node in nodes
  }

  sort_order = []

  while nodes:
    removed_nodes = []
    #O(n)
    for node in nodes:
      if not len(parent_map[node]):
        #O(v)
        for parent_edge_set in parent_map.values():
          if node in parent_edge_set:
            parent_edge_set.remove(node)
        removed_nodes.append(node)
    #O(n)
    for node in removed_nodes:
      sort_order.append(node)
      nodes.remove(node)

    if not removed_nodes:
      raise Exception('Cycle detected')

  return sort_order

class ToposortTestCase(unittest.TestCase):
  def test_should_pass(self):
    sort: List = toposort([
      ('C', 'D'), 
      ('A', 'C'),
      ('A', 'B'),
      ('B', 'C'),
    ])
    print(sort)
    assert sort.index('A') < sort.index('B')
    assert sort.index('A') < sort.index('C')
    assert sort.index('B') < sort.index('C')
    assert sort.index('C') < sort.index('D')

  def test_should_fail_because_cyle(self):
      with self.assertRaises(Exception) as context:
          toposort([
            ('A','B'),
            ('B','A')
          ])

      self.assertTrue('Cycle detected' in str(context.exception))

if __name__ == '__main__':
  unittest.main()