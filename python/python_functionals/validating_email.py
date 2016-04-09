#!/bin/python3

import sys
import re


def check_email(emails):
    pattern = re.compile(r'^[a-zA-Z][\w-]*@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$')
    emails = filter(pattern.match, emails)
    return sorted(emails)

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    emails = []
    for _ in range(n):
        email = sys.stdin.readline().strip()
        emails.append(email)
    print (check_email(emails))
