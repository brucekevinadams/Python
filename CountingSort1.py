# Author: Bruce Adams
# www.austingamestudios.com
# Hackerrank problem
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
