#!/bin/python3


import sys


def number_toys(money, prices):
    total = 0
    nb_toys = 0
    for toy in prices:
        if total + toy < money:
            total += toy
            nb_toys += 1
    return nb_toys

if __name__ == "__main__":
    n, money = list(map(int, sys.stdin.readline().split()))
    prices = sorted(list(map(int, sys.stdin.readline().split())))
    print(number_toys(money, prices))
