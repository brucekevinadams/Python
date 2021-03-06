# Author: Bruce Adams
# www.austingamestudios.com
# Hackerrank problem
#!/bin/python3


import os
import sys
import math

def turan(n,r):
    q,m=divmod(n,r)
    return m*(m-1)//2+(2*m+r*q)*(r-1)*q//2 if m else n*q*(r-1)//2

def search(n,m):
    l,r=1,3*n*n//(n*n-2*m)
    while l<r:
        x=(l+r)//2
        if turan(n,x)>=m: r=x
        else: l=x+1
    return r

for _ in range(int(input())):
    print(search(*map(int,input().split())))
