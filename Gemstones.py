# Author: Bruce Adams
# www.austingamestudios.com
# Hackerrank problem
# Python 3 Program
#!/bin/python3

import math
import os
import random
import re
import sys

print(len(set.intersection(*[set(input()) for _ in range(int(input()))])))
