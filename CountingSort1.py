# Author: Bruce Adams
# www.austingamestudios.com
# Hackerrank problem
# Python 3 Program
# Create Array that should return an array of integers where each value
# is the number of occurrences of the element's index value in the original array. 
#!/bin/python3

import math
import os
import random
import re
import sys

__ = input()

sol = [0] * 100
for i in [int(n) for n in input().split()]:
    sol[i] += 1

print(*sol)
