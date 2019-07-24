#!/bin/python

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    pairs = {}
    pair_count = 0
    for color in ar:
        if color not in pairs or pairs[color] == 0:
            pairs[color] = 1
        elif pairs[color] == 1:
            pair_count += 1
            pairs[color] = 0
    return pair_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    ar = map(int, raw_input().rstrip().split())

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
