#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    a_per_rep = s.count('a')
    quotient = n // len(s)
    remainder = n % len(s)
    remainder_a = s[:remainder].count('a')
    return quotient * a_per_rep + remainder_a

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
