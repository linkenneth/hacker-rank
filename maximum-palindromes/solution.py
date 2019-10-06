#!/bin/python

import math
import os
import random
import re
import sys

from collections import Counter

MOD = 1000000007

def factorial(x, mod):
    result = 1
    for i in xrange(1, x + 1):
        result = (result * i) % mod
    return result


def multInverse(a, mod):
    '''
    Given a PRIME mod p, the multiplicative inverse of a mod p ia a^(p-2) mod p.
    '''
    return pow(a, mod - 2, mod)


def nChooseK(n, k, mod):
    result = 1
    for i in xrange(n - k + 1, n + 1):
        result = (result * i) % mod
    return (result * multInverse(factorial(k, mod), mod)) % mod


#
# Complete the 'initialize' function below.
#
# The function accepts STRING s as parameter.
#

cumFreqs = [Counter()]

def initialize(s):
    # This function is called once before all queries.
    for c in s:
        freqs = cumFreqs[-1].copy()
        freqs[c] += 1
        cumFreqs.append(freqs)

#
# Complete the 'answerQuery' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER l
#  2. INTEGER r
#

def answerQuery(l, r):
    # Return the answer for this query modulo 1000000007.
    freqs = cumFreqs[r] - cumFreqs[l - 1]
    greaterThanTwo = [(k, v) for k, v in freqs.iteritems() if v >= 2]
    oneSideLength = sum(v // 2 for k, v in greaterThanTwo)

    palindromeCount = 1
    for k, v in greaterThanTwo:
        palindromeCount *= nChooseK(oneSideLength, v // 2, MOD)
        palindromeCount %= MOD
        oneSideLength -= v // 2
        freqs[k] -= v // 2 * 2

    centerMultiplier = sum(v for k, v in freqs.iteritems() if v > 0) or 1
    return (palindromeCount * centerMultiplier) % MOD

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    initialize(s)

    q = int(raw_input().strip())

    for q_itr in xrange(q):
        first_multiple_input = raw_input().rstrip().split()

        l = int(first_multiple_input[0])

        r = int(first_multiple_input[1])

        result = answerQuery(l, r)

        fptr.write(str(result) + '\n')

    fptr.close()
