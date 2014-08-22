# Enter your code here. Read input from STDIN. Print output to STDOUT

# Using a segment tree for min range query.
class MinSegmentTree:
    def __init__(self, lst, start = 0):
        ''' NOTE: This tree takes O(n log n) time to construct because of
        the way array slices are handled by copying in Python. There is a
        O(n) time implementation using only views of the elements in the
        list (or indices), but for now this is fine.'''
        self.range = ( start, start + len(lst) - 1 )
        if len(lst) == 1:
            self.data = lst[0]
        else:
            self.left = MinSegmentTree(lst[:len(lst)/2], start = start)
            self.right = MinSegmentTree(lst[len(lst)/2:], start = start + len(lst) / 2)
            self.data = min( self.left.data, self.right.data )

    def min_query(self, start, end):
        ''' Returns the minimum of the elements starting from index
        ``start`` and ending at index ``end``, inclusive. '''
        range_start, range_end = self.range
        if start <= range_start and range_end <= end:
            return self.data
        elif end < range_start or range_end < start:
            return float('inf')
        else:
            return min( self.left.min_query(start, end),
                        self.right.min_query(start, end) )

N, T = [ int(x) for x in raw_input().split() ]
width = [ int(x) for x in raw_input().split() ]
width_tree = MinSegmentTree(width)

for t in range(T):
    i, j = [ int(x) for x in raw_input().split() ]
    print width_tree.min_query(i, j)

