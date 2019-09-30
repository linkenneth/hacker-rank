#!/bin/python

import math
import os
import random
import re
import sys

# Complete the superDigit function below.
def superDigit(n, k):
    if len(n) == 1 and k == 1:
        return n
    s = sum(int(d) for d in n)
    return superDigit(str(s * k), 1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = raw_input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
