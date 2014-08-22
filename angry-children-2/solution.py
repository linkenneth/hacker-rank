# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import deque, defaultdict

class SumQueue:
    ''' Queue that keeps track of the current K items. Also keeps track of
    the sum of the elements in the queue.'''
    def __init__(self):
        self.queue = deque()
        self.sum = 0
    def enqueue(self, x):
        self.queue.append(x)
        self.sum += x
    def dequeue(self):
        x = self.queue.popleft()
        self.sum -= x
        return x
    def first(self):
        return self.queue[0]
    def last(self):
        return self.queue[-1]
    def __len__(self):
        return len(self.queue)

N = int(raw_input())
K = int(raw_input())
packets = []

for n in range(N):
    packets.append(int(raw_input()))

packets.sort()
queue = SumQueue()
L = defaultdict(lambda: 0)

for i, packet in enumerate(packets):
    if i == 0:
        queue.enqueue(packet)
    elif i < K:
        plus = len(queue) * packet - queue.sum
        L[i] = L[i-1] + plus
        queue.enqueue(packet)
    else:
        first = queue.dequeue()
        minus = queue.sum - len(queue) * first
        plus = len(queue) * packet - queue.sum
        L[i] = L[i-1] + plus - minus
        queue.enqueue(packet)
print min(v for k,v in L.items() if k >= K - 1)
