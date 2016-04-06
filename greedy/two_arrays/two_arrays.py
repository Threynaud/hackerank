#!/bin/python3


import sys


def two_arrays(n, k, A, B):
    A.sort(reverse=True)
    B.sort()
    for i in range(n):
        if A[i] + B[i] < k:
            return False
    return True

if __name__ == "__main__":
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        n, k = list(map(int, sys.stdin.readline().split()))
        A = list(map(int, sys.stdin.readline().split()))
        B = list(map(int, sys.stdin.readline().split()))

        if two_arrays(n, k, A, B):
            print("YES")
        else:
            print("NO")
