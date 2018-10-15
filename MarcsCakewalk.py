#!/bin/python3

import math
import os
import random
import re
import sys

input()
print(sum(c * 2 ** j for (j, c) in enumerate(sorted(map(int, input().split()), reverse=True))))
