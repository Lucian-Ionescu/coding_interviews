#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the compareTriplets function below.
def compareTriplets(a, b):
    scores = compareNumbers(a[0], b[0])
    scores = [sum(x) for x in zip(scores, compareNumbers(a[1], b[1]))]
    scores = [sum(x) for x in zip(scores, compareNumbers(a[2], b[2]))]
    return scores


def compareNumbers(a, b):
    if a > b:
        return [1, 0]
    elif a < b:
        return [0, 1]
    return [0, 0]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
