def read_input():
    T = int(raw_input())
    cases = []
    for t in xrange(T):
        N = int(raw_input())
        cases.append(map(int, raw_input().split()))
    return cases

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def solve_case(A):
    if len(A) <= 1:
        return 'NO'
    i = 1
    _gcd = A[0]
    while i < len(A):
        _gcd = gcd(_gcd, A[i])
        if _gcd == 1:
            return 'YES'
        i += 1
    return 'NO'

def main():
    cases = read_input()
    for A in cases:
        print solve_case(A)

if __name__ == '__main__':
    main()
