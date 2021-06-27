#!/bin/python3

import math
import os
import random
import re
import sys

numb = 0

am = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
pm = ['12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '00']



def timeConversion(s):
    
    if s[-2:] == 'AM' and s[:2] != '12':
        
        numb = s[:2]
        numbLessFront = s[:-2]
        finalNumb = numbLessFront[2:]
        
        counter = 0
        # return finalNumb
        for i in am:
            if i != numb:
                counter += 1
            else:
                break
        
        return(f"{am[counter]}{finalNumb}")
    
    elif s[-2:] == 'AM' and s[:2] == '12':
        
        numb = s[:2]
        numbLessFront = s[:-2]
        finalNumb = numbLessFront[2:]
        
        counter = 0
        # return finalNumb
        for i in am:
            if i != numb:
                counter += 1
            else:
                break
        
        return(f"{am[0]}{finalNumb}")
    
    elif s[-2:] == 'PM' and s[:2] == '12':
        numb = s[:2]
        numbLessFront = s[:-2]
        finalNumb = numbLessFront[2:]
        
        counter = 0
        # return finalNumb
        for i in am:
            if i != numb:
                counter += 1
            else:
                break
        
        return(f"{pm[0]}{finalNumb}")
        
    else:
        numb = s[:2]
        numbLessFront = s[:-2]
        finalNumb = numbLessFront[2:]
        
        counter = 0
        
        # return finalNumb
        for i in am:
            if i != numb:
                counter += 1
            else:
                break
        # return str(counter)
        
        return(f"{pm[counter]}{finalNumb}")
        

    
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
    
