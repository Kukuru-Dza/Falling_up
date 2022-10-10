#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def get_fibonacci_number(a):
    if a <= 1:
        return 0
    if a == 2:
        return 1
    a1 = 0
    a2 = 1
    count = 3
    while count <= a:
        a3 = a1 + a2
        a1 = a2
        a2 = a3
        count += 1
    return a3

if __name__ == '__main__':
    number = 20
    print(get_fibonacci_number(number))