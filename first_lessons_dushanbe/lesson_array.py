#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def find_number(a, b):
    if a.count(b) > 0:
        return 1
    else:
        return -1


if __name__ == '__main__':
    number_to_find = int(input('Enter a number: '))
    print(find_number([0, 2, 3, 5], number_to_find))
