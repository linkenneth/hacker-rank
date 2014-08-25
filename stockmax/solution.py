def read_input():
    T = int(raw_input())
    cases = []
    for t in xrange(T):
        N = int(raw_input())
        prices = map(int, raw_input().split())
        cases.append(prices)
    return cases

def solve_case(prices):
    max_price_after = [0] * (len(prices) + 1)
    for day in reversed(xrange(len(prices))):
        max_price_after[day] = max(prices[day], max_price_after[day + 1])

    stock, profit = 0, 0
    for day in xrange(len(prices)):
        if prices[day] == max_price_after[day]:
            profit += stock * prices[day]
            stock = 0
        elif prices[day] < max_price_after[day]:
            profit -= prices[day]
            stock += 1

    return profit

def main():
    cases = read_input()

    for prices in cases:
        print solve_case(prices)

if __name__ == '__main__':
    main()
