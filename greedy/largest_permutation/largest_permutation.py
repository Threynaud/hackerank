#!/bin/python3

import sys

# O(n) to create index and O(k) to make permutations


def biggest_perm(A, n, k):
    nb_perm = 0

    index = [0] * (n + 1)
    for i in range(n):
        index[A[i]] = i

    i = 0
    while nb_perm < k:
        if A[i] != n - i:
            A[index[n - i]] = A[i]
            index[A[i]] = index[n - i]
            A[i] = n - i
            index[n - i] = i
            nb_perm += 1
        i += 1
        if i == n:
            break
    return A


if __name__ == "__main__":
    n, k = list(map(int, sys.stdin.readline().split()))
    A = list(map(int, sys.stdin.readline().split()))
    print(" ".join(map(str, biggest_perm(A, n, k))))
