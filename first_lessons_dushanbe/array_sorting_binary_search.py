#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from array_sorting_bubbles import list_sort


def bin_index(s_a, i):
    if i is None or s_a is None:
        return -1
    elif i < s_a[0] or i > s_a[-1]:
        return -1
    first = 0
    last = len(s_a) - 1
    if i == s_a[first]:
        return first
    elif i == s_a[last]:
        return last
    while first < last:
        mid = (first + last) // 2
        if i == s_a[mid]:
            return mid
        elif i < s_a[mid]:
            last = mid
        elif i > s_a[mid]:
            first = mid




if __name__ == '__main__':
    arr = [-4, 6, 3, 7, 22, 1, -1]
    arr_sorted = list_sort(arr)
    print(arr_sorted)
    ind = 1
    print(bin_index(arr_sorted, ind))