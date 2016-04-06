#!/bin/python3

# Sort each line of the inout matrix and check if columns are sorted


import sys


def is_col_sorted(G, n):
    for j in range(n):
        current = "a"
        for i in range(n):
            if G[i][j] >= current:
                current = G[i][j]
            else:
                return False
    return True

if __name__ == "__main__":
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        n = int(sys.stdin.readline())
        G = []
        for _ in range(n):
            G_t = sorted(list(sys.stdin.readline().strip()))
            G.append(G_t)
        if is_col_sorted(G, n):
            print('YES')
        else:
            print('NO')
