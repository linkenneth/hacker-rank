def read_input():
    n = int(raw_input())
    groups = map(int, raw_input().split())
    return groups

def main():
    groups = read_input()

    sum_up_to = []
    curr_sum = 0
    for group in groups:
        curr_sum += group
        sum_up_to.append(curr_sum)

    sum_up_to_set = set(sum_up_to)
    possible_sizes = set()
    min_size = max(groups)
    for size in sum_up_to:
        if size < min_size:
            continue
        m = 1
        while True:
            multiple = size * m
            if multiple == sum_up_to[-1]:
                possible_sizes.add(size)
                break
            elif multiple > sum_up_to[-1]:
                break
            elif multiple not in sum_up_to_set:
                break
            else:
                m += 1

    possible_sizes = sorted(possible_sizes)
    for size in possible_sizes:
        print size,
                

if __name__ == '__main__':
    main()
