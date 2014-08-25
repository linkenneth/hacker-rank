def read_input():
    T = int(raw_input())
    cases = []
    for t in xrange(T):
        N = int(raw_input())
        stack = map(int, raw_input().split())
        cases.append(stack)
    return cases

def solve_case(stack):
    '''
    Solve by DP.

    Let T(i) = maximum points attainable by playing optimally from the ith
    brick onwards. Then,
        T(i) = max( T(i) - T(i-j) + sum(values[i:i+j+1]) for j in xrange(1, 4) )
    or something like that
    '''
    rest_sum = [0] * (len(stack) + 3)
    curr_sum = 0
    for i, brick in reversed(list(enumerate(stack))):
        curr_sum += brick
        rest_sum[i] = curr_sum

    T = { i : 0 for i in xrange(len(stack), len(stack) + 3) }
    for i in reversed(xrange(len(stack))):
        T[i] = max( rest_sum[i+j] - T[i+j] + sum(stack[i:i+j])
                    for j in xrange(1, 4) )
    return T[0]

def main():
    cases = read_input()

    for stack in cases:
        print solve_case(stack)

if __name__ == '__main__':
    main()
