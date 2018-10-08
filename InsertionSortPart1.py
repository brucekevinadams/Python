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

n=int(input())
arr=[int(x) for x in input().split()]

def insertion_sort(arr):
    e=arr[len(arr)-1]
    ar=arr[0:len(arr)-1]
    l=len(ar)
    last=l-1
    parr=[]
    while last>-1: # 2 4 6 8
        tmp=ar[last]
        if tmp<e:
            break
        parr=ar[0:last]+[tmp]+ar[last:l]     
        
        print (" ".join(str(s) for s in parr))
        last=last-1
    parr[last+1]=e
    print (" ".join(str(s) for s in parr))
    
insertion_sort(arr)