import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, arr):

    # first we sort the array
    arr.sort()

    # we create variable to count the pairs as well as the i position
    pairs = 0
    i = 0

    # lets check how many pairs inside the array
    while i < (n - 1):

        # we check couples of neighbouring elements, if they are equal, we move the index by 2 and add pair amount
        if (arr[i] == arr[i + 1]):
            pairs += 1
            i += 2
        # if they arent pairs, we move the index by 1
        else:
            i += 1

    return pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    result = sockMerchant(n, arr)
    fptr.write(str(result) + '\n')
    fptr.close()


