#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the commonChild function below.
def commonChild(s1, s2):
    '''
    Strategy:

    Construct directed "graph" where letters are vertices and edges are whether
    a letter follows another in the sequence of letters. Size of graph is at
    most O(n) letters and O(n^2) connections.

    Search one graph and match the other. For each path in graph, traverse
    other graph to find matching child string. Each letter in first graph is
    visited only once???
    '''

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
