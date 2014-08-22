# Enter your code here. Read input from STDIN. Print output to STDOUT

import time

N, X = [ int(x) for x in raw_input().split() ]
offers = []

tim = time.time()
import sys
for line in sys.stdin:
    v_i, a_i = [ int(x) for x in line.split() ]
    if a_i <= X:
        offers.append( (v_i, a_i) )
print time.time() - tim
offers.sort(reverse = True)
offers_by_amount = [[] for _ in xrange(X)]
for v_i, a_i in offers:
    offer_list = offers_by_amount[a_i-1]
    if len(offer_list) <= X / a_i:
        offer_list.append( (v_i, a_i) )
offers = [ item for sublist in offers_by_amount for item in sublist ]

N = len(offers)
print N
tim = time.time()
K = {}
K[(0,0)] = 0
for x in xrange(1, X+1):
    K[(0,x)] = -float('inf')

for i in xrange(1, N+1):
    v_i, a_i = offers[i-1]
    for x in xrange(X+1):
        t = K[(i-1, x-a_i)] if x-a_i >= 0 else -float('inf')
        K[(i,x)] = max( K[(i-1, x)], t + v_i )

import sys
print sys.getsizeof(K)
if K[(N,X)] == -float('inf'):
    print 'Got caught!'
else:
    print K[(N,X)]
print (time.time() - tim)
