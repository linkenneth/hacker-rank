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
factorial, and multInverse, there was still a lot of repetitive calculations
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
O(N) work done in the calculation of N! (mod p). We can even memoize the call
to find multiplicative inverse.

See solution3.py for memoized solution.
'''

import math
import os
import random
import re
import sys


MOD = 1000000007

# TODO: can speed up with either memo or "mult range tree"
def factorial(x, mod):
    # print 'factorial', x, mod
    return mTree.getRange(1, x)


# TODO: can we speed this up? seems too unsimilar, and a speedup of only
# log(10^9 + 7).
def multInverse(a, mod):
    '''
    Given a PRIME mod p, the multiplicative inverse of a mod p ia a^(p-2) mod p.
    '''
    # print 'multiInverse', a, mod
    return pow(a, mod - 2, mod)


# TODO: can we speed this up? an "n choose k" segment tree of some sort,
# providing range queries of n choose k? use "mult range" memo of some sort?
# Currently this takes O(n) time total for each query, resulting in
# O(n * q) time total for O(q) queries. This is further slowed by factorial
# taking O(k) time per execution, which is another O(n) time per query
# (repetitive work to be )
def nChooseK(n, k, mod):
    # print 'nChooseK', n, k, mod
    result = mTree.getRange(n - k + 1, n)
    return (result * multInverse(factorial(k, mod), mod)) % mod

#
# Complete the 'initialize' function below.
#
# The function accepts STRING s as parameter.
#

class MultiplicativeRangeTree:
    def __init__(self, l, r, mod=MOD):
        # print 'MultiplicativeRangeTree', l, r
        self.l = l
        self.r = r
        self.mod = mod
        if l >= r:
            self.m = None
            self.result = l
        else:
            self.m = (l + r) // 2
            self.left = MultiplicativeRangeTree(l, self.m, mod=mod)
            self.right = MultiplicativeRangeTree(self.m + 1, r, mod=mod)
            self.result = (self.left.result * self.right.result) % mod

    def getRange(self, l, r):
        '''
        Returns the product of elements l * (l + 1) + (l + 2) + ... + r
        inclusive.
        '''
        if l < self.l or r > self.r:
            raise ValueError('not possible')
        elif l == self.l and r == self.r:
            return self.result
        elif l > self.m:
            return self.right.getRange(l, r)
        elif r <= self.m:
            return self.left.getRange(l, r)
        else:
            return (
                self.left.getRange(l, self.m) *
                self.right.getRange(self.m + 1, r)
            ) % self.mod

cumFreqs = [[0] * 26]
mTree = None

def initialize(s):
    # This function is called once before all queries.
    global mTree

    for c in s:
        freqs = cumFreqs[-1][:]
        freqs[ord(c) - ord('a')] += 1
        cumFreqs.append(freqs)

    palindromeLength = sum(v // 2 for v in freqs if v >= 2)
    mTree = MultiplicativeRangeTree(1, palindromeLength)

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
    # freqs = cumFreqs[r] - cumFreqs[l - 1]
    freqs = [r - l for r, l in zip(cumFreqs[r], cumFreqs[l - 1])]

    palindromeLength = sum(v // 2 for v in freqs if v >= 2)
    palindromeCount = 1
    for i, freq in enumerate(freqs):
        if freq >= 2:
            palindromeCount = (
                (palindromeCount * nChooseK(
                    palindromeLength, freq // 2, MOD)) % MOD
            )
            palindromeLength -= freq // 2
            freqs[i] -= freq // 2 * 2
    centerCount = sum(v for v in freqs if v > 0) or 1
    return (palindromeCount * centerCount) % MOD


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    # print 'starting init'
    initialize(s)
    # print 'init complete'

    q = int(raw_input().strip())

    for q_itr in xrange(q):
        # if q_itr % 100 == 0:
        #     print 'iteration', q_itr
        first_multiple_input = raw_input().rstrip().split()

        l = int(first_multiple_input[0])

        r = int(first_multiple_input[1])

        result = answerQuery(l, r)

        fptr.write(str(result) + '\n')

    fptr.close()
