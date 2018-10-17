#!/bin/python3
import sys

players = "Richard", "Louise"

T = int(input().strip())

for i in range(T):
    N = int(input().strip())
    print(players[bin(N-1).count("1")%2])