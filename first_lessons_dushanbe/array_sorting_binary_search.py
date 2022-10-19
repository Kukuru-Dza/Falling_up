#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from array_sorting_bubbles import list_sort


def bin_index(s_a, i):
    if i is None or s_a is None:
        return -1
    elif len(s_a) == 1:
        return 0
    elif i not in s_a:
        return -1
    elif i == s_a[-1]:
        return len(s_a) - 1

    first = 0
    last = len(s_a) - 1
    mid = (first + last) // 2
    while first < last:
        if i == s_a[mid]:
            return mid
        elif i < s_a[mid]:
            last = mid - 1
        else:
            i > s_a[mid]
        first = mid + 1
        mid = (first + (last - first)) // 2
    return mid



if __name__ == '__main__':
    arr = [5, 4, 3, 2, 1]
    arr_sorted = list_sort(arr)
    print(arr_sorted)
    ind = 4
    print(bin_index(arr_sorted, ind))