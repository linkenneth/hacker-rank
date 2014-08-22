# Enter your code here. Read input from STDIN. Print output to STDOUT

N = int(raw_input())
candies = []

for n in xrange(N):
    candies.append(int(raw_input()))

min_L = [1] * N
min_R = [1] * N

for i in xrange(1, N):
    if candies[i-1] < candies[i]:
        min_L[i] = min_L[i-1] + 1

for i in reversed(xrange(N-1)):
    if candies[i] > candies[i+1]:
        min_R[i] = min_R[i+1] + 1

total = 0

for i in xrange(N):
    total += max(min_L[i], min_R[i])

print total
