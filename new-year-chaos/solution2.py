#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    '''
    Strategy: Count inversions
    -- first, notice that number of people person i must have bribed is the
    number of people with j such that j > i but A[j] < A[i]. In other words,
    the number of people with number less than A[i] but position behind i.
    -- since a single swap can only change this number by 1, we only need to
    count the number of such people.
    -- brute force this is O(n^2). However, we can just iterate backwards from
    the highest number, this way we only need to count total number of people
    behind i. This is O(n).
    -- if at any point the number produced for a particular person is > 2,
    then too chaotic

    ACTUALLY:
    This doesn't work. You don't have information about whether the previous
    number should or should not count towards the next number's count. You can
    achieve what I wanted to originally by removing the element from the array
    after considering the person's count, but this would require a O(n)
    reordering. There are perhaps more complicated methods to make it O(n log n)
    but that would be way too complicated for a simple problem. The method
    used by the sample solution is to just check i-1 and i-2 since a person
    can bribe at most 2 times. This seems unelegant to me, as it seems the
    2-bribe limit was put there solely to make the solution linear, and not
    more complicated.
    '''
    positions = { person: position + 1 for position, person in enumerate(q) }

    totalBribes = 0
    for i in reversed(range(len(q))):
        person = i + 1  # 1-indexed positions
        position = positions[person]
        venalCount = person - position
        if venalCount > 2:
            return 'Too chaotic'
        totalBribes += venalCount
        print(person, position, totalBribes)

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        print(minimumBribes(q))
