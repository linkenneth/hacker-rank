#!/bin/python

import math
import os
import random
import re
import sys

def weight(c):
    return ord(c) - ord('a') + 1

# Complete the weightedUniformStrings function below.
def weightedUniformStrings(s, queries):
    currSum = weight(s[0])
    U = {currSum}
    for i in xrange(len(s) - 1):
        if s[i] == s[i + 1]:
            currSum += weight(s[i + 1])
        else:
            currSum = weight(s[i + 1])
        U.add(currSum)
    return ['Yes' if q in U else 'No' for q in queries]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    queries_count = int(raw_input())

    queries = []

    for _ in xrange(queries_count):
        queries_item = int(raw_input())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
