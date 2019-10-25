#!/bin/python

import math
import os
import random
import re
import sys

# Complete the palindromeIndex function below.
def palindromeIndex(s):
    '''
    Strategy: Greedy.

    At most one index is removed, therefore start by comparing beginning and end
    of strings and take the first mismatch you find to be the character that
    needs to be removed. Keep going to check that the remaining string is a
    palindrome.
    '''
    i = 0
    j = len(s) - 1
    idx = -1
    theRoadLessTaken = None
    while i <= j:
        if s[i] != s[j]:
            if theRoadLessTaken is 'taken':
                # mismatch again, no solution
                return -1
            elif idx >= 0:
                # take the road less taken (second chance)
                if theRoadLessTaken is not None and theRoadLessTaken is not 'taken':
                    i, j = theRoadLessTaken
                    theRoadLessTaken = 'taken'
                    idx = j + 1
            elif s[i + 1] == s[j]:
                idx = i
                theRoadLessTaken = (i, j - 1)
                i += 1
            elif s[i] == s[j - 1]:
                idx = j
                j -= 1
            else:
                return -1  # no solution; more than one mismatch
        else:
            i += 1
            j -= 1
    return idx  # palindrome, or none found

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(raw_input())

    for q_itr in xrange(q):
        s = raw_input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()
