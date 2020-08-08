#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    vals = [0,0,0]
    counter = len(arr)
    for num in arr:
        if num >= 0:
            if num == 0:
                vals[0]+=1 #neu
            else:
                vals[1]+=1 #pos
        else:
            vals[2]+=1 #neg
    print('%.6f' %(vals[1]/counter))
    print('%.6f' %(vals[2]/counter))
    print('%.6f' %(vals[0]/counter))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
