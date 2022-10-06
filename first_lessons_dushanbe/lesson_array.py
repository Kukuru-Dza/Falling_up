#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def find_number(a, b):
    if a is None or b is None:
        return 'failed'

    if a.count(b) > 0:
        # if a.index(b) >= 0:
        return a.index(b)
    else:
        return -1


if __name__ == '__main__':
    number_to_find = int(input('Enter a number: '))
    print(find_number([0, 2, 3, 5, 7], number_to_find))
    print(find_number([0, 2, 3, 5, 7], None))
    print(find_number(None, number_to_find))
