
import math
import os
import random
import re
import sys


def countingValleys(step, paths):

    valley = 0
    seaLevel = 0

    for n in path:
        if n == 'U':
            seaLevel += 1
        else:
            seaLevel -= 1

        if n == 'U' and seaLevel == 0
        valley += 1

    return valley




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
