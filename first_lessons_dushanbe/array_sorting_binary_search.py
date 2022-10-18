#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def list_sort(a):
    if a is None:
        return a
    count = len(a)-1
    while count >= 1:
        ln = 0
        for ln in range(count):
            if a[ln] > a[ln+1]:
                (a[ln], a[ln + 1]) = (a[ln + 1], a[ln])
        count -= 1
    return a


def bin_index(s_a, i):
    if i is None or s_a is None:
        return -1
    elif i > s_a[-1]:
        return -1
    elif i < s_a[0]:
        return -1
    elif len(s_a) == 1:
        return 0
    elif i not in s_a:
        return -1

    mn = 0
    mx = len(s_a)-1
    mid = (mn + (mx-mn)) // 2
    while mn <= mx:
        if i == s_a[mid]:
            return mid
        elif i < s_a[mid]:
            mx = mid - 1
        elif i > s_a[mid]:
            mn = mid + 1
        mid = (mn + (mx-mn)) // 2



if __name__ == '__main__':
    arr = [5, 4, 3, 2, 1]
    arr_sorted = list_sort(arr)
    ind = 4
    print(bin_index(arr_sorted, ind))