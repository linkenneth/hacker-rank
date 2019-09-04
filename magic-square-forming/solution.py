#!/bin/python3

import math
import os
import random
import re
import sys

squares = []
seed = (
    (8, 1, 6),
    (3, 5, 7),
    (4, 9, 2)
)

def reflect(s):
    '''
    Returns a new square that is the reflected version of s.

    Reflects across the identity diagonal. Any sort of reflect works since we
    also rotate.

    >>> rotate(((1, 2, 3),
                (4, 5, 6),
                (7, 8, 9)))
    ((1, 4, 7), (2, 5, 8), (3, 6, 9))
    '''
    return tuple(zip(*s))

def rotate(s):
    '''
    Returns a new square that is s rotated 90 degrees clockwise.

    >>> rotate(((1, 2, 3),
                (4, 5, 6),
                (7, 8, 9)))
    ((7, 4, 1), (8, 5, 2), (9, 6, 3))
    '''
    return tuple(zip(*reversed(s)))

for _ in range(4):
    seed = rotate(seed)
    squares.append(seed)
seed = reflect(seed)
for _ in range(4):
    seed = rotate(seed)
    squares.append(seed)

def squareDiff(a, b):
    '''
    Returns the sum of the absolute values of the differences between each item
    in a and b.
    '''
    return sum(abs(a[i][j] - b[i][j]) for i in range(3) for j in range(3))

# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    '''
    This is an inelegant question. It seems to require preconstructing all magic
    squares ahead of time and comparing them.
    '''
    return min(squareDiff(square, s) for square in squares)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
