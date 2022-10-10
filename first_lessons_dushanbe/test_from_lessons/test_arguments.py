#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def is_contains_char(a, b):
    if a is None or b is None:
        return False
    count = 0
    while count < len(a):
        if b == a[count] or b == a[count].upper() or b == a[count].lower():
            return True
        count += 1
    return False


if __name__ == '__main__':
    a = ('The Tallest tree in the world')
    print(is_contains_char(a, 'E'))


