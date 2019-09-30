#!/bin/python

import math
import os
import random
import re
import sys

from collections import Counter

# Complete the isValid function below.
def isValid(s):
    counter = Counter(s)
    countOfCounts = Counter(counter.values())
    if len(countOfCounts) > 2:
        return 'NO'
    elif len(countOfCounts) <= 1:
        return 'YES'
    print countOfCounts
    mostCommon = countOfCounts.most_common()
    mode, frequency = mostCommon[0]
    nextMode, nextFrequency = mostCommon[1]
    # print mostCommon
    if nextFrequency > 1:
        return 'NO'
    elif nextMode != 1 and abs(mode - nextMode) > 1:
        return 'NO'
    return 'YES'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
