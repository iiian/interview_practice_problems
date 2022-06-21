from test_util import *

# implement a binary search tree
class BST:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

  def contains(self, value) -> bool:
    if value == self.value:
      return True
    if value < self.value:
      if self.left:
        return self.left.contains(value)
      return False
    if self.right:
      return self.right.contains(value)
    return False

  def equals(self, other):
    return (
      self.value == other.value and
      (
        self.left == other.left == None or
        self.left.equals(other.left)
      ) and
      (
        self.right == other.right == None or
        self.right.equals(other.right)
      )
    )

  def to_list(self):
    return (
      (self.left.to_list() if self.left else []) +
      [self.value] + 
      (self.right.to_list() if self.right else [])
    )

  def insert(self, value):
    if value < self.value:
      if self.left:
        return self.left.insert(value)
      self.left = BST(value)
      return
    if self.right:
      return self.right.insert(value)
    self.right = BST(value)

  def remove(self, value):
    return self.__handle_remove(value)

  def __handle_remove(self, value, parent=None):
    # lone root
    if self.left == self.right == parent == None:
      return None
    # value to left
    if value < self.value:
      if self.left: return self.left.__handle_remove(value, self)
      return None
    # value to right
    elif self.value < value: 
      if self.right: return self.right.__handle_remove(value, self)
      return None
    # here it is
    if value == self.value:
      # has no left or right hand child
      if self.left == self.right == None:
        if parent.left == self:
          parent.left = None
        else:
          parent.right = None
      # has left child only
      elif self.left and not self.right:
        self.value = self.left.value
        self.right = self.left.right
        self.left = self.left.left
      elif self.right and not self.left:
        self.value = self.right.value
        self.left = self.right.left
        self.right = self.right.right
      # both left and right
      else:
        # promote right hand min child to the throne
        subst, subst_parent = self.get_next_and_parent(self)
        if self == subst_parent:
          self.value = subst.value
          self.right = self.right.right
          subst.right = None
        else:
          self.value = subst.value
          subst_parent.remove(subst.value)
          
          
  def get_next_and_parent(self, p):
    c = self.right
    while c.left: 
      p = c
      c = c.left
    return c, p

# Test cases

# 1
bst1 = BST(7)
bst1.insert(3)
bst1.insert(3)
bst1.insert(4)
bst1.insert(0)
bst1.insert(10)
bst1.insert(16)
bst1.insert(12)
test(
  True,
  Deferred(BST.contains, bst1, 7)
)
test(
  True,
  Deferred(BST.contains, bst1, 12)
)
test(
  True,
  Deferred(BST.contains, bst1, 3)
)
test(
  False,
  Deferred(BST.contains, bst1, 14)
)
bst2 = BST(7)
bst2.insert(3)
bst2.insert(3)
bst2.insert(4)
bst2.insert(0)
bst2.insert(10)
bst2.insert(16)
bst2.insert(12)
test(
  True,
  Deferred(BST.equals, bst1, bst2)
)
bst1.remove(3)
bst3 = BST(7)
bst3.insert(10)
bst3.insert(3)
bst3.insert(12)
bst3.insert(0)
bst3.insert(16)
bst3.insert(4)
test(
  True,
  Deferred(lambda a,b: a==b, bst1.to_list(), bst3.to_list())
)
bst1.insert(7)
bst3.insert(7)
test(
  True,
  Deferred(lambda a,b: a==b, bst1.to_list(), bst3.to_list())
)
bst3.remove(7)
test(
  False,
  Deferred(lambda a,b: a==b, bst1.to_list(), bst3.to_list())
)
bst1.remove(7)
bst3.remove(17)
test(
  True,
  Deferred(lambda a,b: a==b, bst1.to_list(), bst3.to_list())
)
