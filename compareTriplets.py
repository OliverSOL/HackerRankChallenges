#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.

def compareTriplets(a, b):
    scores = [0,0]
    for n,m in zip(a,b):
        if n > m:
            scores[0]+=1
        elif n < m:
            scores[1]+=1
    return(scores)



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

