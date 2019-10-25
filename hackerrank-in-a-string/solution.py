#!/bin/python

import math
import os
import random
import re
import sys

# Complete the hackerrankInString function below.
def hackerrankInString(s):
    h = 'hackerrank'
    i = 0
    j = 0
    while i < len(h) and j < len(s):
        if h[i] == s[j]:
            i += 1
        j += 1
    return 'YES' if i == len(h) else 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(raw_input())

    for q_itr in xrange(q):
        s = raw_input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()
