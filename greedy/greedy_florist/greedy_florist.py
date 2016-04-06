#!/bin/python3

import sys


def min_price(C, n, k):
    C.sort(reverse=True)
    clients = [1] * k
    curr_client = 0
    total = 0
    for flower in C:
        total += clients[curr_client] * flower
        clients[curr_client] += 1
        curr_client += 1
        if curr_client == k:
            curr_client = 0
    return total

if __name__ == "__main__":
    n, k = list(map(int, sys.stdin.readline().split()))
    C = list(map(int, sys.stdin.readline().split()))
    print(min_price(C, n, k))
