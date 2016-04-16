#!/bin/python3

import sys


def is_funny(s):
    for i in range(1, len(s)):
        if abs(ord(s[i]) - ord(s[i - 1])) != abs(ord(s[-i]) - ord(s[-i - 1])):
            return False
            break
    return True

if __name__ == "__main__":
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        s = sys.stdin.readline().strip()
        if is_funny(s):
            print("Funny")
        else:
            print("Not Funny")
