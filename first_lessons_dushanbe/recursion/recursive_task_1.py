#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def rec(a):
    if len(a) == 1:
        return a
    else:
        return a[0] + '*' + rec(a[1:])


if __name__ == '__main__':
    s = input('Enter: ')
    print(rec(s))
