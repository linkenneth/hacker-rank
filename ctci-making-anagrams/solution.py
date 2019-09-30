#!/bin/python

import math
import os
import random
import re
import sys

from collections import Counter

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    countA = Counter()
    countB = Counter()
    for s, count in [(a, countA), (b, countB)]:
        for c in s:
            if c not in count:
                count[c] = 0
            count[c] += 1
    return (
        sum((countA - countB).values()) +
        sum((countB - countA).values()))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = raw_input()

    b = raw_input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
