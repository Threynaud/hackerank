#!/bin/python3


import sys

if __name__ == "__main__":
    s = set(sys.stdin.readline().strip().lower().replace(" ", ""))
    if len(s) == 26:
        print("pangram")
    else:
        print("not pangram")
