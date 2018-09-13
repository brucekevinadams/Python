# Author: Bruce Adams
# www.austingamestudios.com
# Hackerrank problem
#!/bin/python3

import math
import os
import random
import re
import sys

n = int(input().strip())
numbers = list(map(int, input().strip().split()))
myDict = {}
for i in range(n):
  myDict[numbers[i]] = i
minCost = 10 ** 10
nums = sorted(myDict)
for i in range(1, n):
  if (nums[i] - nums[i - 1] < minCost) and(myDict[nums[i]] < myDict[nums[i - 1]]):
    minCost = nums[i] - nums[i - 1]
print(minCost)
