#!/bin/python3


import sys


def order_orders(n, orders):
    l = sorted([(order_id + 1, orders[order_id][0] + orders[order_id][1])
                for order_id in range(n)], key=lambda x: (x[1], x[0]))
    return [order[0] for order in l]

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    orders = []
    for _ in range(n):
        order = tuple(map(int, sys.stdin.readline().split()))
        orders.append(order)
    print(" ".join(map(str, order_orders(n, orders))))
