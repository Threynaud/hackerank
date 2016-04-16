#!/bin/python3

import sys


if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    gems = []
    for _ in range(n):
        gems.append(set(sys.stdin.readline().strip()))
    print(len(set.intersection(*gems)))
