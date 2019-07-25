#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    index = { x : i for i, x in enumerate(arr) }
    x = 1
    swaps = 0
    while x < len(arr) + 1:
        i = x - 1  # where it should be
        j = index[x]  # where it is right now
        # print(arr, index, i, j)
        if i != j:
            index[arr[i]], index[arr[j]] = j, i
            arr[i], arr[j] = arr[j], arr[i]
            swaps += 1
        x += 1
    return swaps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
