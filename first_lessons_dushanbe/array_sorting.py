#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def list_sort(a):
    if a is None:
        return False
    lst = []
    ln = len(a)
    while len(lst) < ln:
        min_val = a[0]
        for elt in a:
            if elt < min_val:
                min_val = elt
        lst.append(min_val)
        a.remove(min_val)
    return lst


if __name__ == '__main__':
    arr = None
    #arr = [-4, 6, 3, 7, 22, 1, 1, 1, -1]
    print(list_sort(arr))