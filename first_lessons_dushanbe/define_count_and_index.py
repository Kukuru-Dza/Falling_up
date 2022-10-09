#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def fn_count(a, b):
    #if a is None or b is None:
    #    return 0
    x = 0
    count = 0
    while x < len(a):
        if b == a[x]:
            count += 1
        x += 1
    return count


def fn_index(a, b):
    #if a is None or b is None:
    #    return False
    x = 0
    while x < len(a):
        if b == a[x]:
            return x
        x += 1
    return False


if __name__ == '__main__':
    print(fn_index([1, 3, 'abc', 9], 'abc'))
    print(fn_count([1, 3, 'abc', 9], 'abc'))
    print(fn_index([1, 3, None, 5] , None))
    print(fn_count([1, 3, None, 5] , None))