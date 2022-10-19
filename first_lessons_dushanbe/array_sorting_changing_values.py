#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def list_sort(a):
    if a is None:
        return a
    count = 0
    while count < len(a)-1:
        ln = len(a) - 1
        while ln > count:
            if a[ln] < a[ln-1]:
                a[ln], a[ln-1] = a[ln-1], a[ln]
            ln -= 1
        count += 1
    return a

if __name__ == '__main__':
    arr = [5, 4, 3, 2, 1]
    print(list_sort(arr))