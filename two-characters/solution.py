#!/bin/python

import math
import os
import random
import re
import sys

from itertools import combinations

# Complete the alternate function below.
def alternate(s):
    '''
    Strategy: brute force. For each of the (26 choose 2) ways of selecting
    two characters, try to construct a string and see if it's a maximum
    length string. 325 * 1000 is feasible.

    Also slight optimizations by instantly disqualifying any character that has
    adjacent characters.
    '''
    # print s
    charset = set(s)

    dqChars = set()
    for i in xrange(len(s) - 1):
        if s[i] == s[i + 1]:
            dqChars.add(s[i])
    # print 'dqChars', dqChars

    maxLen = 0
    for a, b in combinations(charset, 2):
        # print 'a, b', a, b
        if a in dqChars or b in dqChars:
            continue
        last = None
        length = 0
        dq = False
        for c in s:
            # print 'last, length, c', last, length, c
            if c != a and c != b:
                continue
            elif last is not None and c == last:
                dq = True
                break
            # print 'setting last to', c
            last = c
            length += 1
        if not dq and length > maxLen:
            maxLen = length
    return maxLen

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(raw_input().strip())

    s = raw_input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
