#!/bin/python

import math
import os
import random
import re
import sys

def transpose(x):
    return zip(*x)

# Complete the organizingContainers function below.
def organizingContainers(container):
    containerSizes = [sum(balls) for balls in container]
    ballCounts = [sum(type) for type in transpose(container)]
    return 'Possible' if sorted(containerSizes) == sorted(ballCounts) else 'Impossible'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(raw_input())

    for q_itr in xrange(q):
        n = int(raw_input())

        container = []

        for _ in xrange(n):
            container.append(map(int, raw_input().rstrip().split()))

        result = organizingContainers(container)

        fptr.write(result + '\n')

    fptr.close()
