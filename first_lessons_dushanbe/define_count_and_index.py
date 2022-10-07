#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def fn_count(a, b):
    if a is None or b is None:
        return 0
    x = 0
    count = 0
    while x < len(a):
        if b == a[x]:
            count += 1
        x += 1
    return count


def fn_index(a, b):
    if a is None or b is None:
        return False
    x = 0
    count = 0
    # return x if b == a[x] else x += 1 - не работает
    while x < len(a) and count == 0:
        if b == a[x]:
            count += 1
            return x
        else:
            x += 1
    return False


if __name__ == '__main__':
    print(fn_count([0, 2, 3, 2, 5, 2, 7], 2))
    print(fn_count([0, 2, 3, 2, 5, 2, 7], 5))
    print(fn_count([0, 2, 3, 2, 5, 2, 7], 8))
    print(fn_count([0, 2, 3, 2, 5, 2, 7], None))
    print(fn_count(None, 2))
    print('')
    print(fn_index([0, 2, 3, 2, 5, 2, 7], 2))
    print(fn_index([0, 2, 3, 2, 5, 2, 7], 5))
    print(fn_index([0, 2, 3, 2, 5, 2, 7], 8))
    print(fn_index([0, 2, 3, 2, 5, 2, 7], None))
    print(fn_index(None, 2))