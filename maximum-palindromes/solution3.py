#!/bin/python

'''
Redo to make it more efficient and cleaner.

There were a few issues with the original version:
(1) not correctly performing modular arithmetic at every step, leading to
increasing input size for large inputs
(2) use of Counter() was probably slow

This version seeks to fix that. Instead of dividing by factorial(k) in
nChooseK, we find the multiplicative inverse modulo 10^9 * 7 so that we can
also do this step in modular arithmetic correctly.

------------------------------------

After testing, the algorithm is still not fast enough to pass. After debugging,
I found that the issue is that, even with proper mod math on nChooseK,
factorial, and inverse, there was still a lot of repetitive calculations
happening.

n in nChooseK is on the order of O(n / 2). For each query q, nChooseK takes
O(n) time total as it iterates from n down to n-k, all the way down to 0.
In addition, factorial takes O(k) every execution of nChooseK, for a total
of O(n) per query. We need to make these two O(1) or O(log n) time in order
to pass the time limit.

The best way to do this is to create a multiplicative range query tree, and
pre-calculate partial factorials modulo 10^9 + 7.

------------------------------------

I did it but it's still too slow? I think it's because in the original
formulation in version 1 I decided to use the N choose K method, to avoid
doing modular division. Instead, I can use the factorial / divide duplicates
formulation.

A quick calculation shows that for Q = 10^5, the tree is of depth ~14. Each
N choose K operation traverses this tree of depth 14 and needs to perform up
to 14 multiplications. This happens against with the call to factorial.
Finally, this is done up to 26 times for each letter of the alphabet.

Instead, if we calculate N! / (a!b!...z!) where a, b, c are the number of
duplicates, we can simplify and get rid of the tree, and use a simple memoized
solution. Each factorial call is done in constant time, and there is at most
O(N) work done in the calculation of N! (mod p). We can also optimize by
only finding the multiplicative inverse of the entire denominator once.

Final clean version below.
'''

import math
import os
import random
import re
import sys


MOD = 1000000007

factorialCache = [1, 1]
def factorial(x, mod):
    if x < len(factorialCache):
        return factorialCache[x]
    result = factorialCache[-1]
    for i in xrange(len(factorialCache), x + 1):
        factorialCache.append((factorialCache[-1] * i) % mod)
    return factorialCache[x]


def inverse(a, mod):
    '''
    Given a PRIME mod p, the multiplicative inverse of a mod p ia a^(p-2) mod p.
    '''
    return pow(a, mod - 2, mod)

#
# Complete the 'initialize' function below.
#
# The function accepts STRING s as parameter.
#

cumFreqs = [[0] * 26]

def initialize(s):
    # This function is called once before all queries.
    for c in s:
        freqs = cumFreqs[-1][:]
        freqs[ord(c) - ord('a')] += 1
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
    freqs = [r - l for r, l in zip(cumFreqs[r], cumFreqs[l - 1])]

    palindromeLength = sum(v // 2 for v in freqs if v >= 2)
    palindromeCount = factorial(palindromeLength, MOD)
    denom = 1
    for i, freq in enumerate(freqs):
        if freq >= 2:
            denom = (denom * factorial(freq // 2, MOD)) % MOD
    centerCount = sum(1 for v in freqs if v % 2) or 1
    return (
        palindromeCount * inverse(denom, MOD) * centerCount
    ) % MOD


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
