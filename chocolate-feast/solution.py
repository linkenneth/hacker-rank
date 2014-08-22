# Enter your code here. Read input from STDIN. Print output to STDOUT

T = int(raw_input())
for t in range(T):
    N, C, M = [ int(x) for x in raw_input().split() ]
    chocolates = wrappers = N / C
    while wrappers >= M:
        exchanges = wrappers / M
        chocolates += exchanges
        wrappers -= (M - 1) * exchanges
    print chocolates
