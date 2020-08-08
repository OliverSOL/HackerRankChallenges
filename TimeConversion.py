#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    timeAM = s[-2:].lower() == 'am' #returns True if time in am, otherwise false
    if timeAM and s[:2] == "12": #converts hours to 0 if its AM and 12
        return "00" + s[2:-2]
    elif timeAM: # time format remains w/o the am/pm value
        return s[:-2]
    elif not timeAM and s[:2] == "12": #if PM and hr = 12 time format sticks
        return s[:-2]
    else: # if hr is less than 12, add 12 to adjust to 24hr format and concatenate values
        return str(int(s[:2]) + 12) + s[2:8] 
    

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
