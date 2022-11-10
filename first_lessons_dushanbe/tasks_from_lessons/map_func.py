#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''Write a Python program to triple all numbers of a given list of integers. Use Python map'''


def triple(i):
    return int(i) * 3


if __name__ == '__main__':
    a = list(input().split())
    b = list(map(triple, a))
    print(b)
    c = list(map(lambda x: (int(x) * 3), a))
    print(c)
