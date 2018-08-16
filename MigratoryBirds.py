#!/bin/python

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.

def migratoryBirds(n, ar):
    m = [4,3,2,1,0]
    for b in ar:
        m[b-1] += 10
    return 5 - max(m) % 10

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(raw_input().strip())

    arr = map(int, raw_input().rstrip().split())

    result = migratoryBirds(arr_count, arr)

    fptr.write(str(result) + '\n')

    fptr.close()