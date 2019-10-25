#!/bin/python

import math
import os
import random
import re
import sys

def rotate(A, i):
    A[i:i + 2], A[i + 2] = A[i + 1:i + 3], A[i]

# Complete the larrysArray function below.
def larrysArray(A):
    for _ in xrange(len(A)):
        for i in xrange(len(A) - 2):
            while A[i] != min(A[i], A[i + 1], A[i + 2]):
                rotate(A, i)
    return 'YES' if sorted(A) == A else 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(raw_input())

    for t_itr in xrange(t):
        n = int(raw_input())

        A = map(int, raw_input().rstrip().split())

        result = larrysArray(A)

        fptr.write(result + '\n')

    fptr.close()
