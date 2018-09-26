# Author: Bruce Adams
# www.austingamestudios.com
# Hackerrank problem
#!/bin/python3

import math
import os
import random
import re
import sys

for _ in range(int(input())):
    _, arr = input(), [int(n) for n in input().split()]
    h = m = t = arr[0]
    for ind, n in enumerate(arr):
        if ind == 0: continue
        t = max(t, n, t + n)
        h = max(n, h + n)
        m = max(m, h)
    print(m, t)
