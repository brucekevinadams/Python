

import math
import os
import random
import re
import sys

from collections import Counter
input()
a,b=[[int(i) for i in input().split()] for _ in range(2)]
c = Counter(a)- Counter(b)
s = sum(v for v in c.values())
if s == 0:
    s+=2
print(len(a)-s+1)