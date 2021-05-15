#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    i = 0
    while (i < n):
        i += 1

    stairPos = int(i)
    stairFill = 0

    while stairPos > 0:
        stairPos -= 1
        stairFill += 1
        print(' ' * stairPos + '#' * stairFill)

if __name__ == '__main__':
    n = int(input())

    staircase(n)
