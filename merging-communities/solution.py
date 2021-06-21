'''
Use disjoint set forests to implement three operations:
(1) union, merges two set forests into a larger one
(2) find, finds whether a person is in this discrete set forest
(3) size, returns the size of this set forest
'''

class DisjointSetForest:
  def __init__(self):
    self.items = {}

  def make_set(self, x):
    '''
    Adds `x` to the forest.
    '''
    if x not in self.items:
      n = Node(x)
      self.items[x] = n

  def find(self, x):
    '''
    Using "path splitting", a form of path compression, finds the root node that
    `x` belongs to and also replace every parent pointer on this path to point
    to the node's grandparents. This helps amortized O(N log* N) time.
    '''
    while x.parent != x:
      x, x.parent = x.parent, x.parent.parent
    return x

  def union(self, x, y):
    '''
    Merges the sets belonging to `x` and to `y`.
    '''
    x = self.find(x)
    y = self.find(y)
    if x == y:
      return

    if x.size < y.size:
      y, x = x, y # x is always the larger set

    y.parent = x
    x.size = x.size + y.size

class Node:
  def __init__(self, value):
    self.value = value
    self.parent = self
    self.size = 1

def merge(x, y):
  x, y = forest.items[x], forest.items[y]
  forest.union(x, y)

def query(x):
  x = forest.items[x]
  print(forest.find(x).size)

if __name__ == '__main__':
  N, Q = [int(x) for x in input().split()]

  forest = DisjointSetForest()
  for n in range(N):
    forest.make_set(n + 1)

  for q in range(Q):
    operation, *operands = input().split()
    if operation == 'M':
      merge(*[int(x) for x in operands])
    elif operation == 'Q':
      query(*[int(x) for x in operands])
    else:
      raise 'wtf'
