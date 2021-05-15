import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr.sort()
    miniSum = 0
    maxiSum = 0

    for i in arr[:-1]:
        miniSum += i

    for e in arr[1:]:
        maxiSum += e

    print(int(miniSum), int(maxiSum))


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
