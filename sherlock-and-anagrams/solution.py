#!/bin/python

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    '''
    Plan: Use sliding window to record character compositions of substrings.
    Take total substring composition frequencies and compute anagram pair
    count with (n choose 2) where n in the frequency of substring anagram.

    Time: O(n^3 log n) lol...

    There are O(n^2) substrings. O(n) different start lengths. O(n) different
    start locations. Must not use O(n) to recreate each substring or to hash.
    Can use O(1) time for start and end index to reference it.
    '''
    anagramCount = {}
    for length in xrange(1, len(s)):
        for i in xrange(len(s) - length + 1):
            anagram = ''.join(sorted(s[i:i + length]))
            if anagram not in anagramCount:
                anagramCount[anagram] = 0
            anagramCount[anagram] += 1
    totalCount = 0
    for anagram, count in anagramCount.items():
        if count > 1:
            totalCount += choose(count, 2)
    return totalCount

def choose(n, k):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(raw_input())

    for q_itr in xrange(q):
        s = raw_input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
