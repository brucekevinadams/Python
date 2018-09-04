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

# Complete the morganAndString function below.
def morganAndString(a, b):
    answer = ''
    a += '~'
    b += '~'
    i = 0
    j = 0
    while a[i] != '~' or b[j] != '~':
        if a[i] != '~' and a[i:] < b[j:]:
            answer += a[i]
            i += 1
        else:
            answer += b[j]
            j += 1
    return answer  


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        a = input()

        b = input()

        result = morganAndString(a, b)

        fptr.write(result + '\n')

    fptr.close()
