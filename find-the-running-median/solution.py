#!/bin/python

import os
import sys

import heapq

def getMedian(maxHeap, minHeap):
    if not maxHeap and not minHeap:
        return None
    elif len(maxHeap) > len(minHeap):
        return -maxHeap[0]
    elif len(maxHeap) < len(minHeap):
        return minHeap[0]
    else:
        return (-maxHeap[0] + minHeap[0]) / 2.

#
# Complete the runningMedian function below.
#
def runningMedian(a):
    maxHeap, minHeap = [], []
    median = None
    for item in a:
        if not median or item < median:
            heapq.heappush(maxHeap, -item)
            if len(maxHeap) > len(minHeap) + 1:
                heapq.heappush(minHeap, -heapq.heappop(maxHeap))
        else:
            heapq.heappush(minHeap, item)
            if len(minHeap) > len(maxHeap) + 1:
                heapq.heappush(maxHeap, -heapq.heappop(minHeap))
        median = getMedian(maxHeap, minHeap)
        if median:
            yield float(median)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(raw_input())

    a = []

    for _ in xrange(a_count):
        a_item = int(raw_input())
        a.append(a_item)

    result = runningMedian(a)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
