#!/bin/python3


import sys

# O(nlog(n)) solution


def number_units(W, n):
    W.sort()
    curr = W[0]
    units = 1
    for i in range(1, n):
        if W[i] not in range(curr, curr + 5):
            curr = W[i]
            units += 1
    return

# Greedy O(n) solution


def number_units2(W, n):
    m_w = max(W) + 1
    units = 0
    visited = [0] * m_w
    for toy in W:
        visited[toy] = 1

    i = 0
    while i < m_w:
        if visited[i] > 0:
            units += 1
            i += 4
        i += 1
    return units


if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    W = list(map(int, sys.stdin.readline().split()))
    print(number_units2(W, n))
