#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def is_contains_char(a, b):
    count = 0
    x = 0
    while count < len(a) or x == 1:
        if b == a[count] or b == a[count].upper() or b == a[count].lower():
            x += 1
        count += 1

    if x > 0:
        return True
    else:
        return False


if __name__ == '__main__':
    a = ('The Tallest tree in the world')
    print(is_contains_char(a, 'E'))


