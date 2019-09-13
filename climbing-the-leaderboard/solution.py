#!/bin/python

'''
Reflection on this question:

I definitely overcomplicated the question. Considering that there are O(m)
queries all in descending order, we can find the answer to all of them in O(n)
time. There is no need to do binary search, which could in fact be slower
at O(m log n) time. Even with my optimization to start at a lower "high" every
time, it is not guaranteed to be better than the linear solution, though it
is probably likely.

In general, while binary search provides great speed for single queries @
O(log n), it unfortunately takes O(m log n) for O(m) queries. On the other hand,
if there is an order to the queries (or we can order it in O(m log m) time),
then the ordered queries can be performed simply in O(m) time.
'''

import math
import os
import random
import re
import sys

def findRanking(scores, aScore, low=None, high=None):
    # print aScore
    if low is None:
        low = 0
    if high is None:
        high = len(scores) - 1

    while low <= high:
        mid = (low + high) // 2
        # print low, mid, high
        # print low, mid, high:
        if aScore == scores[mid]:
            return mid + 1
        elif scores[mid] > aScore:
            low = mid + 1
        else:
            high = mid - 1
    mid = (low + high + 1) // 2
    return mid + 1

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    # remove duplicates
    # rScores = reduce(
    #     lambda x, y: x if x[-1] == y else x + [y], scores, [scores[0]])
    rScores = []
    currentScore = None
    for score in scores:
        if currentScore is None or score != currentScore:
            rScores.append(score)
            currentScore = score
    # print 'rScores:', len(rScores)

    # repeatedly binary search leaderboard for Alice's position and
    # corresponding ranking. Use information about previous highest location
    # to reduce search space for binary search.
    aRankings = []
    low, high = 0, len(rScores) - 1
    for aScore in alice:
        if len(aRankings) > 0:
            high = min(aRankings[-1] - 1, len(rScores) - 1)
        aRankings.append( findRanking(rScores, aScore, high=high) )
    return aRankings

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(raw_input())

    scores = map(int, raw_input().rstrip().split())

    alice_count = int(raw_input())

    alice = map(int, raw_input().rstrip().split())

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
