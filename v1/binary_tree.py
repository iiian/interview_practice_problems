class Node:
  def __init__(self, value, left = None, right = None):
    self.value = value
    self.left = left
    self.right = right

  def insert(self, value):
    if value < self.value:
      if not self.left:
        self.left = Node(value)
      else:
        self.left.insert(value)
    else:
      if not self.right:
        self.right = Node(value)
      else:
        self.right.insert(value)

  def remove(self, value, parent = None):
    if self.value < value:
      if not self.right: return None
      return self.right.remove(value, self)
    if value < self.value:
      if not self.left: return None
      return self.left.remove(value, self)

    del_target = self
    if del_target.right:
      succ_val = del_target.right.getLeast()
      del_target.value = succ_val
      return del_target.right.remove(succ_val)

    elif del_target.left:
      pred_val = del_target.left.getLargest()
      del_target.value = pred_val
      return del_target.left.remove(pred_val)
    
    elif not del_target.right and not del_target.left:
      if not parent: return None
      if parent.left == del_target:
        parent.left = None
      else:
        parent.right = None
      return

  def getLargest(self):
    if self.right: return self.right.getLargest()
    return self.value

  def getLeast(self):
    if self.left: return self.left.getLeast()
    return self.value

  def has(self, value):
    if self.value == value:
      return True
    if self.value < value:
      return self.right and self.right.has(value)
    if value < self.value:
      return self.left and self.left.has(value)

class NodeFactory:
  def create(values):
    first, *rest = values
    node = Node(first)
    for value in rest:
      node.insert(value)
    return node

if __name__ == "__main__":
  # insertion tests
  node = NodeFactory.create([1,6,3,8,2,0])
  assert(node.value == 1)
  assert(node.left.value == 0)
  assert(node.right.value == 6)
  assert(node.right.left.value == 3)

  # has tests
  assert(node.has(8))
  assert(not node.has(10))
  assert(node.has(1))

  # removal tests
  node.remove(16)
  node.remove(0)
  assert(not node.left)
  node.insert(0)