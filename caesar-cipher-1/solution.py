#!/bin/python

import math
import os
import random
import re
import sys

# Complete the caesarCipher function below.
def caesarCipher(s, k):
    cipher = []
    for i, c in enumerate(s):
        o = ord(c)
        if o >= ord('a') and o <= ord('z'):
            cipher.append(chr((o - ord('a') + k) % 26 + ord('a')))
        elif o >= ord('A') and o <= ord('Z'):
            cipher.append(chr((o - ord('A') + k) % 26 + ord('A')))
        else:
            cipher.append(c)
    return ''.join(cipher)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    s = raw_input()

    k = int(raw_input())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
