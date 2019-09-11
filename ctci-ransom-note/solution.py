#!/bin/python

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    wordCounts = {}
    for word in magazine:
        if word not in wordCounts:
            wordCounts[word] = 0
        wordCounts[word] += 1
    for word in note:
        if word not in wordCounts or wordCounts[word] == 0:
            print 'No'
            return
        wordCounts[word] -= 1
    print 'Yes'
    return

if __name__ == '__main__':
    mn = raw_input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = raw_input().rstrip().split()

    note = raw_input().rstrip().split()

    checkMagazine(magazine, note)
