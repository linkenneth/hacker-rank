#!/bin/python

import math
import os
import random
import re
import sys

import bisect

# Complete the activityNotifications function below.
def activityNotifications(expenditures, d):
    '''
    Strategy: Maintain a sorted list / binary tree

    Maintain a sorted list of size D. Index D / 2 is the median. For each new
    value, find the value D time ago and remove it from sorted list in O(log n)
    time.

    Only problem here is how to maintain a sorted list that can insert and
    delete in O(log n) time. Consider a skip list or a rebalancing sorted tree.

    For now, let's assume Python sort has good runtime for an almost-sorted
    list.
    '''
    window = []
    median = None

    notifCount = 0
    for i, expenditure in enumerate(expenditures):
        if len(window) < d:
            window.append(expenditure)
            window.sort()
        else:
            j = bisect.bisect(window, expenditures[i - d - 1])
            print(j, window, expenditures[i - d - 1], expenditures)
        # add new to list
            # check median and determine notification

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = raw_input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = map(int, raw_input().rstrip().split())

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
