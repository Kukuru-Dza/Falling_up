#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from first_lessons_dushanbe.sortings.array_sorting_bubbles import list_sort


def bin_index(s_a, i):
    if i is None or s_a is None:
        return -1
    elif i not in s_a:
        return -1

    first = 0
    last = len(s_a) - 1
    if i == s_a[first]:
        return first
    elif i == s_a[last]:
        return last
    first += 1
    last -= 1
    while first <= last:
        mid = (first + last) // 2
        if i < s_a[mid]:
            last = mid
        elif i == s_a[mid]:
            return mid
        elif i > s_a[mid]:
            first = mid
        else:
            return -1


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 8, 17, 22]
    arr_sorted = list_sort(arr)
    print(arr_sorted)
    ind = 5
    print(bin_index(arr_sorted, ind))
