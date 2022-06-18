"""A simple Tree class implementation """
from dataclasses import dataclass
from typing import Any

@dataclass
class Tree:
  """A simple Tree class"""
  value: Any
  left: Any = None
  right: Any = None

  def insert(self, value) -> None:
    """Insert a node into the tree"""
    cursor = self
    while True:
      if cursor.value <= value:
        if cursor.right:
          cursor = cursor.right
        else:
          cursor.right = Tree(value)
          return
      elif value < cursor.value:
        if cursor.left:
          cursor = cursor.left
        else:
          cursor.left = Tree(value)
          return    

  def remove(self, value) -> bool:
    """Remove a node from the tree if it exists."""
    # go searching for this value
    parent: Any = None
    cursor: Any = self
    while cursor:
      if cursor.value < value:
        parent = cursor
        cursor = cursor.right
      elif value < cursor.value:
        parent = cursor
        cursor = cursor.left
      else:
        break
    if not cursor or (not parent and not cursor.left and not cursor.right):
      return False

    #LR|
    #00| Evict, notify parent of death of child (need to check whether its left or right)
    if not cursor.left and not cursor.right:
      if parent.left == cursor:
        parent.left = None
      else:
        parent.right = None
    #01| Move right onto cursor, adopt its children
    elif not cursor.left:
      cursor.value = cursor.right.value
      cursor.left = cursor.right.left
      cursor.right = cursor.right.right
    #10| Move left onto cursor, adopt its children
    elif not cursor.right:
      cursor.value = cursor.left.value
      cursor.right = cursor.left.right
      cursor.left = cursor.left.left
    #11| Replace with leftmost child of right tree, make self.right=self.right.right, and evict leftmost child
    else:
      def get_leftmost_child(c, p):
        while c.left:
          p, c = c, c.left
        return c, p
      # successor should have no left child,
      successor, parent_successor = get_leftmost_child(cursor.right, cursor)
      cursor.value = successor.value
      if cursor == parent_successor:
        cursor.right = successor.right
      else:
        # if successor is not cursor's right child, i.e.:
        #   o <- cursor
        #    \
        #     o <- parent_successor
        #    / \...
        #   o <- successor
        #    \... <- successor.right
        # then parent_successor.left == successor, by definition.
        parent_successor.left = successor.right
    return True


  def contains(self, value) -> bool:
    """Does the tree contain this node"""
    cursor = self
    while cursor:
      if cursor.value < value:
        cursor = cursor.right
      elif value < cursor.value:
        cursor = cursor.left
      else:
        return True
    return False

if __name__ == '__main__':
    tree = Tree(8)
    tree.insert(4)
    tree.insert(12)
    tree.insert(2)
    tree.insert(1)
    tree.insert(3)
    tree.insert(10)
    tree.insert(9)
    tree.insert(11)
    tree.insert(14)
    tree.insert(15)
    tree.insert(13)
    tree.insert(17)

    assert tree.value == 8
    assert tree.left.value == 4
    assert tree.right.value == 12
    assert tree.left.left.value == 2
    assert tree.right.left.value == 10, f'tree.right.left.value was {tree.right.left.value}'
    assert tree.contains(4)
    assert tree.contains(8)
    assert tree.contains(11)

    assert tree.remove(7) == False
    assert tree.remove(8) == True
    assert tree.value == 9, f'tree.value was {tree.value}'
    assert tree.remove(15) == True
    assert tree.right.right.right.value == 17, f'was {tree.right.right.right}'
    assert tree.remove(12) == True
    assert tree.value == 9, f'tree.value was {tree.value}'
    assert tree.contains(12) == False
    assert tree.remove(9) == True
    assert tree.contains(9) == False
    assert tree.value == 10
    assert tree.right.left.value == 11