# Enter your code here. Read input from STDIN. Print output to STDOUT

N = int(raw_input())
K = int(raw_input())
packets = []
for n in range(N):
    packets.append( int(raw_input()) )

packets.sort()
min_unfairness = float('inf')
for i in range(len(packets)-K):
    if packets[i+K-1] - packets[i] < min_unfairness:
        min_unfairness = packets[i+K-1] - packets[i]

print min_unfairness
