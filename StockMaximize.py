# Author: Bruce Adams
# www.austingamestudios.com
# Hackerrank problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the stockmax function below.

def stockmax(prices):
    price = 0
    cost = 0
    income = 0
    for i in range(len(prices)-1,-1,-1):
        if price < prices[i]:
            price = prices[i]
        else:
            cost += prices[i]
            income += price
    return income-cost

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        prices = list(map(int, input().rstrip().split()))

        result = stockmax(prices)

        fptr.write(str(result) + '\n')

    fptr.close()
