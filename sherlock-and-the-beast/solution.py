def read_input():
    T = int(raw_input())
    cases = []
    for t in xrange(T):
        cases.append(int(raw_input()))
    return cases

def solve_case(case):
    for num_3 in xrange(0, 15, 5):
        num_5 = case - num_3
        if num_5 % 3 == 0:
            break
    if not 0 <= num_3 <= case:
        return '-1'
    return '5' * num_5 + '3' * num_3

def main():
    cases = read_input()
    for case in cases:
        print solve_case(case)

if __name__ == '__main__':
    main()
