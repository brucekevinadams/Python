#!/bin/python3

import math
import os
import random
import re
import sys

n = int(input().strip())
for i in range(n):    
    option = int(input().strip())
    print("Second" if option % 7 in [0, 1] else "First")