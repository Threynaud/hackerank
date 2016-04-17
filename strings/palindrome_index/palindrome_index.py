#!/bin/python3

import sys


def palindrome_index(s):
    is_palindrome = lambda s: True if s == s[::-1] else False
    if is_palindrome(s):
        return -1
    for i in range(len(s)):
        if s[i] != s[-i - 1]:
            if is_palindrome(s[:i] + s[i + 1:]):
                return i
                break
            else:
                return len(s) - i - 1
                break

if __name__ == "__main__":
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        s = sys.stdin.readline().strip()
        print(palindrome_index(s))
