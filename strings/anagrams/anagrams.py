#!/bin/python3

import sys
from collections import Counter


def anagrams(s):
    if len(s) % 2 != 0:
        return -1
    mid = len(s) // 2
    total = 0
    count_letters = dict(Counter(list(s[:mid])))
    for letter in s[mid:]:
        if (letter in count_letters) and (count_letters[letter] > 0):
            count_letters[letter] -= 1
        else:
            total += 1
    return total

if __name__ == "__main__":
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        s = sys.stdin.readline().strip()
        print(anagrams(s))
