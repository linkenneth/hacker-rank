# Enter your code here. Read input from STDIN. Print output to STDOUT

# This problem was really hard. The key is to realize that the problem can
# be thought of as its inverse -- that is, the maximum profit obtained must
# also correspond to the minimum loss incurred (all while keeping to the
# at-most-k-boards constaint).
#
# Keeping this in mind, we can reformulate a different dynamic program
# that's easier to deal with. Let L(i) be the minimum loss incurred by
# removing the billboard at position i and removing billboards at the
# optimal positions from positions 1...i-1. Then,
# L(i) = P[i] + min( L(j) | j = i-k-1...i-1 )
#
# The latter expression min( L(j) | j = i-k-1...i-1 ) is just a running
# minimum of width k, so we can use some kind of method to amortize the
# running time of this. Thus, we no longer need the full O(nk) time implied
# by the recursion itself. In fact, we realize that because (1) the
# algorithm seems to run through the solution once (in linear time) and (2)
# each L(i) only depends on L(i-k-1...i-1), we only need to keep a data
# structure of the last k elements. It would also be convenient if this
# data structure kept track of the running minimum as required.
#
# At first, a heap-like priority queue structure comes to mind. At each
# step you find the minimum L(j) of the current window (O(1)), remove the
# oldest value L(i-k-1) in the window (let's say that by some miraculous
# hashing trick this is O(logk) time as well), and insert the newly
# calculated value L(i) (O(logk)). As we calculate all L(i) up to L(n),
# thus this process takes O(nlogk) time and O(k) space. However, we can do
# faster.
#
# Notice that for any j1 < j2, if L(j1) > L(j2), then L(j1) cannot be the
# minimum in the window anymore. This is because (1) as long as L(j2) is in
# the window, L(j2) will always be a better minimum than L(j1), and (2)
# L(j1) will be removed first from the window. Thus we can remove L(j1)
# from the window / queue. This suggests that, every time we insert some
# value L(j2), we can check all previous values L(j1) in the window to see
# if they can be removed from being considered. What values need to be
# checked? By induction, if we do this process every time, then every value
# remaining in the window, when arranged in the order of their indices j,
# should be in sorted order! We simply need to check values backwards from
# L(j2) and remove values until we see some L(j1) that has L(j1) <= L(j2),
# at which point we stop. This is basically stack-based sorting.
#
# With this, the minimum of the window is simply the first value in the
# queue / stack. At each step, we remove the oldest value L(i-k-1) if it's
# still in the queue. We also insert a new value L(i) at each step which
# can result in the removal of many previous values in the queue. However,
# amortized, each value is inserted and removed exactly once. Thus this
# method takes O(1) amortized time, such that the final algorithm takes
# O(n) time and O(k) space. A bit of extra book-keeping may be necessary to
# keep track of the indices of the values still in the queue, but this does
# not affect the running time.

from collections import deque

class QueueAndMinQueue:
    ''' Two queues in one -- one that acts like a normal queue, and one
    that keeps track of the current minimum. Results in basically a queue
    to keeps track of the min amongst its elements.'''
    def __init__(self):
        self.queue = deque()
        self.min_queue = deque()
    def enqueue(self, x):
        self.queue.append(x)
        while self.min_queue and self.min_queue[-1] > x:
            self.min_queue.pop()
        self.min_queue.append(x)
    def dequeue(self):
        x = self.queue.popleft()
        if x == self.min_queue[0]:
            self.min_queue.popleft()
        return x
    def first(self):
        return self.queue[0]
    def last(self):
        return self.queue[-1]
    def min(self):
        return self.min_queue[0]
    def __len__(self):
        return len(self.queue)

N, K = [ int(x) for x in raw_input().split() ]
profits = []
for n in range(N):
    profits.append( int(raw_input()) )

queue = QueueAndMinQueue()
queue.enqueue(0)

for i, p in enumerate(profits):
    if len(queue) > K + 1:
        queue.dequeue()  # remove L(i-k-1)
    L_i = profits[i] + queue.min()
    queue.enqueue(L_i)
if len(queue) > K + 1:
    queue.dequeue()

print sum(profits) - queue.min()  # min loss => max profit
