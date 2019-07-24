#!/bin/python3

import math
import os
import random
import re
import sys

def isTooChaotic(q):
    for position, person in enumerate(q):
        if person - (position + 1) > 2:
            return True
    return False

# Complete the minimumBribes function below.
def minimumBribes(q):
    '''
    Strategy: Greedy
    -- first, check is it's too chaotic. Too chaotic means a single person
    is AHEAD of their original place by more than two spots. For example,
    23451 is not too chaotic, but 51234 is.
    -- then, greedily simulate swapping by exchanging the highest most out of
    place pair
    -- stop when ordered or 2n exceeded
    '''
    if isTooChaotic(q):
        return 'Too chaotic'

    persons = q[:]
    positions = { person: position + 1 for position, person in enumerate(q) }
    def swap(personA, personB):
        positionA = positions[personA]
        positionB = positions[personB]
        if positionA - positionB > 1 or positionA - positionB < -1:
            raise ValueError('oh shit')
        positions[personA] = positionB
        positions[personB] = positionA
        persons[positionA - 1] = personB
        persons[positionB - 1] = personA

    operations = 0
    limit = 2 * len(q)
    currentPerson = max(persons)
    while currentPerson and operations < limit:
        currentPosition = positions[currentPerson]
        # print(currentPerson, currentPosition, persons, positions)
        if currentPerson == currentPosition:
            currentPerson -= 1
            continue
        if currentPerson > persons[currentPosition - 1 + 1]:
            swap(currentPerson, persons[currentPosition - 1 + 1])
            operations += 1
        else:
            raise ValueError('something went wrong')
    if operations >= limit:
        return 'Too chaotic'
    return operations

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        print(minimumBribes(q))
