#!/bin/python3

import sys


def min_cost(Y, X):
    x_cuts = 1  # Number of segments along Y
    y_cuts = 1  # Number of segments along X
    total = 0  # Total cost
    X.sort(reverse=True)
    Y.sort(reverse=True)

    while len(Y) > 0 and len(X) > 0:
        if X[0] >= Y[0]:
            x_cuts += 1
            total += X[0] * y_cuts
            X.pop(0)
        else:
            y_cuts += 1
            total += Y[0] * x_cuts
            Y.pop(0)

    while len(X) > 0:
        total += X[0] * y_cuts
        X.pop(0)

    while len(Y) > 0:
        total += Y[0] * x_cuts
        Y.pop(0)
    return total % (10**9 + 7)

if __name__ == "__main__":
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        m, n = list(map(int, sys.stdin.readline().split()))
        Y = list(map(int, sys.stdin.readline().split()))
        X = list(map(int, sys.stdin.readline().split()))
        print(min_cost(Y, X))
