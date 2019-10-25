#!/bin/python

# TODO: if bored, implement all 4 solutions to this problem.

import math
import os
import random
import re
import sys

# Complete the activityNotifications function below.
def activityNotifications(expenditures, d):
    '''
    This problem effectively requires you to find the sliding window median.
    There are at least four possible solutions to this:

    (1) Median heap. Using a min-heap and a max-heap, keep track of the running
    median. As elements in the window expire, theoretically, we should remove
    the element from one of the two heaps. However, although deleting is
    O(log n), finding the element in the heap is O(n). To not incur O(n^2) time
    complexity, we need to do some kind of special accounting in the sizes of
    the heaps to "soft delete" elements. Total time complexity: O(n log n)
    (2) Bucketed counts. Given that the range of the elements is limited to 0 <=
    expenditures[i] <= 200, we can keep the count of each of the elements in
    this range. As elements in the window expire, simply decrement the count.
    We can brute-force over these counts and find the median in O(k) time, where
    k is the range of expenditures[i] (in this case, ~200). Total time
    complexity: O(nk)
    (3) Segment / range tree. Similar to (2) but use a segment / range tree
    instead. Don't need to brute force over O(k) elements, but insertion into
    the tree now takes O(log k) time. More complex than (2) but potentially
    faster, but no longer uses contiguous memory. Total time complexity:
    O(n log k).
    (4) Self-balancing BST. Stick elements of a window in a self-balancing
    BST (ie. auto-sorted array), maintaining sorted order in O(log n). Find
    the median in O(1) time by finding the middle element / root element.
    This is similar to the median heap solution otherwise. Total time
    complexity: O(n log n)

    See intense-interviews/running-median for details on all four methods.
    '''
    counts = [0] * 201
    window = 0
    notifications = 0
    for i, expenditure in enumerate(expenditures):
        if window < d:
            window += 1
        else:
            # brute force over buckets
            totalCount = 0
            low = high = None
            for j, count in enumerate(counts):
                # if count is not 0:
                #     print j, count, totalCount
                totalCount += count
                if low is None and totalCount >= (d - 1) // 2 + 1:
                    low = j
                if totalCount >= d // 2 + 1:
                    high = j
                if high is not None:
                    break
            median = (low + high) / 2.
            if expenditure >= 2 * median:
                notifications += 1
            counts[expenditures[i - d]] -= 1
        counts[expenditure] += 1
    return notifications

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = raw_input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = map(int, raw_input().rstrip().split())

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
