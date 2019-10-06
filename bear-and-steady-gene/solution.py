#!/bin/python

import math
import os
import random
import re
import sys

from collections import Counter

# Complete the steadyGene function below.
def steadyGene(gene):
    '''
    Strategy: "slinky" algorithm.

    Shortest substring that contains at least a given set of elements
    can be completed in linear time with a sort of "slinky" algorithm.
    Essentially, keep two pointers, one for the end of the string and one
    for the beginning. Try to increment the end of the string, then if the
    current string encounters an element that we need to include, "pull"
    the beginning pointer forwards maximally until this the shortest possible
    string that fulfills the condition ending at the end of the string is
    found. Record into array like DP.

    Not bad. Interesting problem.
    '''
    L = [0] * len(gene)

    # first, find the minimum set of required amino acids
    target = len(gene) / 4
    freqs = Counter({ 'A': -target, 'C': -target, 'G': -target, 'T': -target })
    for c in gene:
        freqs[c] += 1
    for k, v in freqs.items():
        if v <= 0:
            del freqs[k]

    curr = Counter({ k: 0 for k in freqs.keys() })
    if len(curr) == 0:
        return 0

    # next, find the shortest substring that contains these AAs ending at
    # each letter
    i = 0
    j = 0
    while j < len(gene):
        if gene[j] in freqs:
            curr[gene[j]] += 1
            while all(curr[k] >= freqs[k] for k in freqs.keys()):
                if gene[i] in freqs:
                    curr[gene[i]] -= 1
                    L[j] = j - i + 1
                i += 1
        j += 1
    return min(filter(lambda x: x > 0, L))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    gene = raw_input()

    result = steadyGene(gene)

    fptr.write(str(result) + '\n')

    fptr.close()
