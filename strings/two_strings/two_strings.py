#!/bin/python3

import sys

if __name__ == "__main__":
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        A = set(sys.stdin.readline().strip())
        B = set(sys.stdin.readline().strip())
        if set.intersection(A, B):
            print("YES")
        else:
            print("NO")
