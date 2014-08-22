# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(raw_input())
A = [ int(x) for x in raw_input().split() ]
m = int(raw_input())
B = [ int(x) for x in raw_input().split() ]

from collections import defaultdict
b_counts = defaultdict(lambda: 0)

for x in B:
    b_counts[x] += 1

a_counts = defaultdict(lambda: 0)

for x in A:
    a_counts[x] += 1

missing = []
keys = set(b_counts)
for key in keys:
    if a_counts[key] != b_counts[key]:
        missing.append( str(key) )

print ' '.join(sorted(missing))
