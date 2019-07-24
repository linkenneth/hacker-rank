def read_input():
    N = int(raw_input())
    rocks = []
    for n in xrange(N):
        rocks.append(raw_input().strip())
    return rocks

def main():
    rocks = read_input()
    rock_compositions = [set(rock) for rock in rocks]

    min_length = min(len(rock) for rock in rock_compositions)
    for rock in rock_compositions:
        if len(rock) == min_length:
            min_rock = rock
            break

    gem_elements = 0
    for element in min_rock:
        if all(element in rock for rock in rock_compositions):
            gem_elements += 1

    print gem_elements

if __name__ == '__main__':
    main()
