#!/bin/python

import copy

# Head ends here
def insertionSort(ar):
    v = ar[-1]
    ar[-1] = None
    print_with_none(ar, v)
    for i in reversed(range(len(ar) - 1)):
        if ar[i] > v:
            ar[i], ar[i+1] = ar[i+1], ar[i]
            print_with_none(ar, v)
        else:
            ar[i+1] = v
            print_with_none(ar, v)
            return

def print_with_none(a, v):
    a = copy.copy(a)
    prev = v
    for i, x in enumerate(a):
        if x is None:
            a[i] = prev
        prev = x
    print ' '.join(str(x) for x in a)

# Tail starts here

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)
