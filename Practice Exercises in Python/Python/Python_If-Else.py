#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    
    checkedN = n % 2

    if (checkedN == 0 and 2 <= n <= 5):
        #print(checkedN)
        print("Not Weird")
    elif (checkedN == 0 and 6 <= n <= 20):
        #print(checkedN)
        print("Weird")
    elif (checkedN == 0 and n > 20):
        #print(checkedN)
        print("Not Weird")
    else:
        #print(checkedN)
        print("Weird")
