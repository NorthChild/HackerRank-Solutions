#!/bin/python3

import os
import sys

#
# Complete the simpleArraySum function below.
#   
def simpleArraySum(ar):
    x = 0
    y = 0
    if (x < len(ar)):
        for i in ar:
            x += 1
            y = y + i
    return y

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
