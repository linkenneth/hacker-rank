#!/bin/python

import math
import os
import random
import re
import sys

from collections import defaultdict

# Complete the countTriplets function below.
def countTriplets(arr, r):
    '''
    Some examples:
    1 2 4 8 16
    1 1 1

    1 2 3 4 6 12
    3 2 3 1 2 1

    1 2 4 8 4 8 16
    5 4 3 2 3 2 1
    2   2

    1 1 1 1
    4 3 2 1

    4 2 1 8
    should be 0

    1 2 2 1 4
    should be 2

    Ideas:
    (1) Dynamic programming (sort of). Let L(i) be the length of geometric
    progression starting at i.

    L(i) = L(j) + 1 if L(j) / L(i) == r for all i < j
         = L(j) if i == j (going upwards)

    Then, how to find triplets?

    (2) See a number, put in hash map. Check if previous two in sequence already
    seen, as well as count. 1 1 2 2 4 is 2 * 2 triplets. But fails for 2 2 1 4.

    (3) Similar to (2), except first do doublets, then do triplets. But no.
    '''
    # triplets = 0
    # counts = {}
    # for ak in arr:
    #     ai, aj = float(ak) / (r * r), float(ak) / r
    #     if ai in counts and aj in counts:
    #         if ai == aj:
    #             triplets += counts[ai] * (counts[aj] - 1) / 2
    #         else:
    #             triplets += counts[ai] * counts[aj]
    #     if ak not in counts:
    #         counts[ak] = 0
    #     counts[ak] += 1
    # return triplets
    # TODO: this doesn't work yet
    triplets = 0
    counts = defaultdict(lambda: 0)
    D = defaultdict(lambda: 0)
    for ak in arr:
        ai, aj = float(ak) / (r * r), float(ak) / r
        if aj in counts:
            D[ak] += counts[aj]
            if ai in counts:
                # if ai == aj:
                #     triplets +=
                triplets += counts[ai] * D[aj]
        counts[ak] += 1
    print D
    return triplets

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = raw_input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = map(long, raw_input().rstrip().split())

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
