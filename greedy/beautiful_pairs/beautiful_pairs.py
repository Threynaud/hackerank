#!/bin/python3


import sys


def beautiful_pairs(A, B, n):
    """ Loop over B. If element is also in A, remove from A
    """
    # A_t = tuple(A)
    B_t = tuple(B)
    for elem in B_t:
        if elem in A:
            A.remove(elem)
    if len(A) == 0:
        # If A=B, have to remove 1 element
        return n - 1
    else:
        return len(B_t) - len(A) + 1


if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    A = list(map(int, sys.stdin.readline().split()))
    B = list(map(int, sys.stdin.readline().split()))
    print (beautiful_pairs(A, B, n))
