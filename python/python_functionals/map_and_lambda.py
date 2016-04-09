#!/bin/python3


import sys


def fibonnacci(n):
    fib = [0, 1]
    if n == 0:
        return []
    elif n == 1:
        return [0]
    [fib.append(fib[-1] + fib[-2]) for _ in range(n - 2)]
    return fib

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    print(list(map(lambda x: x ** 3, fibonnacci(n))))
