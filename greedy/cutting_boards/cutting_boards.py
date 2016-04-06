#!/bin/python3

import sys


def min_cost(m, n, Y, X):
    h_cuts = 0  # Number of cuts along Y
    v_cuts = 0  # Number of cuts along X
    total = 0  # Total cost
    X.sort()
    Y.sort()


if __name__ == "__main__":
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        m, n = list(map(int, sys.stdin.readline().split()))
        Y = list(map(int, sys.stdin.readline().split()))
        X = list(map(int, sys.stdin.readline().split()))
        print(min_cost(m, n, Y, X))
