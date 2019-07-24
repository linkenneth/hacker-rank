def read_input():
    N, K = map(int, raw_input().split())
    prices = map(int, raw_input().split())
    return prices, K

def main():
    prices, K = read_input()
    prices.sort(reverse=True)
    toys = 0
    while K >= prices[-1]:
        prices.pop()
        toys += 1
    print toys

if __name__ == '__main__':
    main()
