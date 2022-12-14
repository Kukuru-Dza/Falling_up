#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def list_sort(a):
    if a is None:
        return a
    count = len(a) - 1
    while count >= 1:
        ln = 0
        for ln in range(count):
            if a[ln] > a[ln + 1]:
                a[ln], a[ln + 1] = a[ln + 1], a[ln]
        count -= 1
    return a


if __name__ == '__main__':
    arr = [4, 3, 2, 1]
    print(list_sort(arr))
