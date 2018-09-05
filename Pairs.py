# Author: Bruce Adams
# www.austingamestudios.com
# email: ezaroth@gmail.com
# Hackerrank problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pairs function below.
def pairs(k, a):
    d = {}
    answer = 0
    for i in a:
        d[i] = i
    for j in a:
        g = j+k
        if g in d:
            answer +=1
    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
