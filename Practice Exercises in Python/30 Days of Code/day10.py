
import math
import os
import random
import re
import sys

# finding consecutive integers
def find_max_ones(num):
    result = len(max(num.replace('0', ' ').split(), key=len))
    return result

# important variables
revBinary = []
strBinary = ''


if __name__ == '__main__':
    
    n = int(input())
    ogNum = n

    # here we convert the number into binary
    while (n > 1):
        x = n % 2
        x = math.floor(x)
        revBinary.append(x)
        n = n / 2

    # we reverse the list to visualise the actual binary conversion in a list
    binary = list(reversed(revBinary))
    # print("Binary of " + str(ogNum) + " : " + str(binary), end="\n ")

    # then we transform the list to a string
    for i in revBinary:
        strBinary = strBinary + str(i)
    # print(int(strBinary))

    # then we find the consecutive 1's in the string
    binCount = find_max_ones(strBinary)
    print(binCount)



