#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    positives = 0
    negatives = 0
    zeros = 0

    arrLen = len(arr)

    for element in arr:
        if (element > 0):
            positives += 1
        elif (element == 0):
            zeros += 1
        else:
            negatives += 1


    positiveRateo = (positives / arrLen)
    negativeRateo = negatives / arrLen
    zerosRateo = zeros / arrLen
    print("{:.6f}".format(positiveRateo))
    print("{:.6f}".format(negativeRateo))
    print("{:.6f}".format(zerosRateo))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
