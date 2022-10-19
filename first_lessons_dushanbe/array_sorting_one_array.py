#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def list_sort(a):
    if a is None:
        return a
    count = 0
    while count < len(a) - 1:
        count1 = count
        min_val = a[count1]
        while count1 < (len(a) - 1):
            if a[count1 + 1] < min_val:
                min_val = a[count1 + 1]
                ind_min_val = count1 + 1
            count1 += 1
        a.remove(a[ind_min_val])
        a.insert(count, min_val)
        count += 1
    return a


if __name__ == '__main__':
    arr = [5, 4, 3, 2, 1]
    print(list_sort(arr))
