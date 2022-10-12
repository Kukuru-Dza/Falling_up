#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from define_count_and_index import fn_index


def find_number(a, b):
    if a is None or b is None:
        return -1

    x = fn_index(a, b)
    if x >= 0:
        return x
    else:
        return -1


if __name__ == '__main__':
    number_to_find = int(input('Enter a number: '))
    print(find_number([0, 2, 3, 5, 7], number_to_find))
    print(find_number([0, 2, 3, 5, 7], None))
    print(find_number(None, number_to_find))
