# Enter your code here. Read input from STDIN. Print output to STDOUT

N = int( raw_input() )
lst = [ int(x) for x in raw_input().split() ]
lst.sort()
m = float('inf')
ms = []
for i in range(len(lst) - 1):
    diff = lst[i+1] - lst[i]
    if diff < m:
        m = diff
        ms = [ ( lst[i], lst[i+1] ) ]
    elif diff == m:
        ms.append( ( lst[i], lst[i+1] ) )

print ' '.join( '%d %d' % x for x in ms )
