# Solution that works. This solution ends up just being a modified UCS
# (uniform cost search). Whereas normal search just uses a "visited" set,
# with these changes, you will have to use a dictionary that denotes the
# number of times a certain node was visited. In the very very worst case
# it's possible that the algorithm runs in O(nm(n+m)) time ( O(nm) for
# board scan, up to O(n+m) moves total ), but in most cases it is much less
# than that.
#
# The way the algorithm works is sort of like UCS -- for each number of
# changes, the first time a node is visited must be the shortest distance
# to that node USING A CERTAIN NUMBER OF CHANGES. That means that each node
# is expanded at most TOTAL_MOVES times, most of the time much less using
# backtracking data.

import collections
from Queue import PriorityQueue

def make_board(n, m):
    return [[None] * m for _ in xrange(n)]

def print_board(board):
    for row in board:
        print ''.join(str(c) if c is not None else 'x' for c in row)

def compute_forward_dist(board, max_changes=0):
    n, m = len(board), len(board[0])
    forward_dist = make_board(n, m)
    visited = collections.defaultdict(lambda: -1)
    queue = PriorityQueue()
    queue.put((0, 0, 0, 0))  # (changes, dist, i, j)

    while not queue.empty():
        changes, dist, i, j = queue.get()
        if forward_dist[i][j] is None:
            forward_dist[i][j] = dist
        else:
            forward_dist[i][j] = min(forward_dist[i][j], dist)
        direction = board[i][j]
        if visited[(i, j)] >= changes:
            continue
        if direction == '*':
            if changes == max_changes:
                break
            else:
                continue
        visited[(i, j)] = changes
        delta_i, delta_j = direction_to_delta(direction)
        if visited[(i + delta_i, j + delta_j)] < changes \
          and (0 <= i + delta_i < n and 0 <= j + delta_j < m):
            queue.put(
                (changes, dist + 1, i + delta_i, j + delta_j)
            )

        for direction_ in all_directions():
            if changes == max_changes:
                break
            elif direction_ == direction:
                continue
            delta_i, delta_j = direction_to_delta(direction_)
            if visited[(i + delta_i, j + delta_j)] < changes \
              and (0 <= i + delta_i < n and 0 <= j + delta_j < m):
                queue.put(
                    ((changes + 1), dist + 1, i + delta_i, j + delta_j)
                )

    return forward_dist

def direction_to_delta(direction):
    if direction == 'U':
        return (-1, 0)
    elif direction == 'L':
        return (0, -1)
    elif direction == 'D':
        return (1, 0)
    elif direction == 'R':
        return (0, 1)

def all_directions():
    return 'ULDR'

def read_input():
    N, M, K = map(int, raw_input().split())
    board = []
    for n in xrange(N):
        row = [c for c in raw_input().strip()]
        board.append(row)
    return N, M, K, board

def direct_dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def main():
    N, M, K, board = read_input()

    target = None
    for i, row in enumerate(board):
        if not target:
            for j, cell in enumerate(row):
                if cell == '*':
                    target = (i, j)
                    target_i, target_j = target
                    break

    if direct_dist((0, 0), target) > K:
        print -1
        return

    max_changes = 0
    while True:
        forward_dist = compute_forward_dist(board, max_changes=max_changes)
        dist_to_target = forward_dist[target_i][target_j]
        # print 'CHANGES: {}'.format(max_changes)
        # print_board(forward_dist)
        if dist_to_target is not None and int(dist_to_target) <= K:
            print max_changes
            break
        max_changes += 1

if __name__ == '__main__':
    main()
