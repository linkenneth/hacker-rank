""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def checkBST(root):
  '''
  This seems like a dumb challenge. This definition does not seem right.
  '''
  if not root:
    return True
  left_values = traverse(root.left)
  right_values = traverse(root.right)
  all_values = left_values + [root.data] + right_values
  if len(all_values) != len(set(all_values)):
    return False
  elif not all(left < root.data for left in left_values):
    return False
  elif not all(right > root.data for right in right_values):
    return False
  return checkBST(root.left) and checkBST(root.right)

def traverse(node):
  '''
  Returns all the data values of a tree.
  '''
  if not node:
    return []
  data = []
  stack = [node]
  while len(stack) > 0:
    node = stack.pop()
    data.append(node.data)
    if node.left:
      stack.append(node.left)
    if node.right:
      stack.append(node.right)
  return data
