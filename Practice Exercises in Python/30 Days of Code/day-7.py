

import math
import os
import random
import re
import sys

finOutput = " "


if __name__ == '__main__':
    n = int(input())

    list = list(map(int, input().rstrip().split()))

    revList = list[::-1]

    for i in revList:
        finOutput += (str(i) + " ")

    finOutput = finOutput[1:]
    print(finOutput)

