#!/bin/python3

import sys


def nb_deletions(s):
    curr = s[0]
    tot = 1
    for i in s[1:]:
        if i != curr:
            curr = i
            tot += 1
    return(len(s) - tot)

if __name__ == "__main__":
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        s = sys.stdin.readline().strip()
        print(nb_deletions(s))
