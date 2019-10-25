#!/bin/python

import math
import os
import random
import re
import sys

# Complete the gridlandMetro function below.
def gridlandMetro(n, m, k, track):
    trackByRow = {}
    for r, c1, c2 in track:
        if r not in trackByRow:
            trackByRow[r] = []
        trackByRow[r].append((c1, 'astart'))
        trackByRow[r].append((c2, 'end'))

    nonEmptyTracks = sorted(trackByRow.keys())
    lamps = n * m
    for i, r in enumerate(nonEmptyTracks):
        trackByRow[r].sort()
        trackStack = []
        for c, type in trackByRow[r]:
            if type == 'astart':
                trackStack.append(c)
            elif type == 'end':
                c1 = trackStack.pop()
                if not trackStack:
                    lamps -= c - c1 + 1
            else: assert 0
    return lamps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nmk = raw_input().split()

    n = int(nmk[0])

    m = int(nmk[1])

    k = int(nmk[2])

    track = []

    for _ in xrange(k):
        track.append(map(int, raw_input().rstrip().split()))

    result = gridlandMetro(n, m, k, track)

    fptr.write(str(result) + '\n')

    fptr.close()
