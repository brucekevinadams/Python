# Author: Bruce Adams
# www.austingamestudios.com
# Hackerrank problem
#!/bin/python3

import os
import sys

#
# Complete the bricksGame function below.
#

def bricksGame(arr):
    lenarr = len(arr)
    dp = [0] * (lenarr + 1)
    bricks = list(reversed(arr))
    suma =  [0] * (lenarr + 1)
    for i in range(1,len(arr)+1):
        suma[i] = suma[i-1] + bricks[i-1]
        if i <= 3:
            dp[i] = sum(bricks[:i])
        else:
            a = bricks[i-1] - dp[i-1] + suma[i-1]
            b = sum(bricks[i-2:i]) - dp[i-2] + suma[i-2]
            c = sum(bricks[i-3:i]) - dp[i-3] + suma[i-3]
            dp[i] = max(a,b,c)
    return dp[lenarr]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        arr_count = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = bricksGame(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
