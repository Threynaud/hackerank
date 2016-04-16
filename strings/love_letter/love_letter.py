#!/bin/python3

import sys


def nb_operations(s):
    total = 0
    for i in range(len(s) // 2):
        total += abs(ord(s[i]) - ord(s[-i - 1]))
    return total

if __name__ == "__main__":
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        s = sys.stdin.readline().strip()
        print(nb_operations(s))
