class Board:
    def __init__(self, board):
        self.board = board
        self.destination = None
        for i, row in enumerate(board):
            if not self.destination:
                for j, cell in enumerate(row):
                    if cell == '*':
                        self.destination = (i, j)
                        break

        self.n = len(board)
        self.m = len(board[0])
        self.forward_dist = [[None] * self.m for _ in xrange(self.n)]
        self.backward_dist = [[None] * self.m for _ in xrange(self.n)]

    @classmethod
    def print_board(cls, board):
        for row in board:
            print ''.join(str(c) if c is not None else 'x' for c in row)

    def compute_forward_dist(self):
        dist = 0
        i, j = 0, 0
        while 0 <= i < self.n and 0 <= j < self.m:
            self.forward_dist[i][j] = dist
            direction = self.board[i][j]
            if direction == '*':
                break
            delta_i, delta_j = self.direction_to_delta(direction)
            i += delta_i
            j += delta_j
            dist += 1

    def compute_backward_dist(self):
        for initial_direction in 'ULDR':
            i, j = self.destination
            self.backward_dist[i][j] = 0
            delta_i, delta_j = self.direction_to_delta(initial_direction)
            i -= delta_i
            j -= delta_j
            dist = 1
            while 0 <= i < self.n and 0 <= j < self.m:
                self.backward_dist[i][j] = dist
                direction = self.board[i][j]
                if direction == '*':
                    break
                delta_i, delta_j = self.direction_to_delta(direction)
                i -= delta_i
                j -= delta_j
                dist += 1

    def direction_to_delta(self, direction):
        if direction == 'U':
            return (-1, 0)
        elif direction == 'L':
            return (0, -1)
        elif direction == 'D':
            return (1, 0)
        elif direction == 'R':
            return (0, 1)

def read_input():
    N, M, K = map(int, raw_input().split())
    board = []
    for n in xrange(N):
        row = raw_input().strip()  # efficiency
        board.append(row)
    return N, M, K, Board(board)

def main():
    N, M, K, board = read_input()
    board.compute_forward_dist()
    board.compute_backward_dist()
    board.print_board(board.forward_dist)
    board.print_board(board.backward_dist)

if __name__ == '__main__':
    main()
