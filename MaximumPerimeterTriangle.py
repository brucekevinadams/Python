# Author: Bruce Adams
# email: ezaroth@gmail.com
# website: austingamestudios.com
# Python 3 program
# Hackerrank problem
# Given an array of stick lengths, use 3 of them to construct a non-degenerate triange
# with the maximum possible perimeter. Print the lengths of its sides as 3 space-separated
# integers in non-decreasing order.
#
# If there are several valid triangles having the maximum perimeter:
#
# Choose the one with the longest maximum side.
# If more than one has that maximum, choose from them the one with the longest minimum side.
# If more than one has that maximum as well, print any one them.
#
# If no non-degenerate triangle exists, print -1.
#
#!/bin/python3

import math
import os
import random
import re
import sys

n = int(input())
A = sorted(int(i) for i in input().split())

i = n-3
while i >= 0 and (A[i] + A[i+1] <= A[i+2]) :
    i -= 1

if i >= 0 :
    print(A[i],A[i+1],A[i+2])
else :
    print(-1)
