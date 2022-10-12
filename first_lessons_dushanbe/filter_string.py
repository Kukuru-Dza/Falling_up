#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def space_trim(a):
    if a is None:
        return a
    while a[0] == ' ':
        a = a[1:]
    while a[-1] == ' ':
        a = a[:-1]
    return a


def filter_string(a, b):
    if a is None:
        return a
    a = space_trim(a)
    if b is None:
        return a
    output_string = ''
    b = b.lower()
    for item in a:
        if b != item.lower():
            output_string += item
    # эквивалентно
    # inx = 0
    # for _ in a:
    #     if b != a[inx].lower():
    #         output_string += a[inx]
    #     inx += 1
    return output_string


if __name__ == '__main__':
    text = '       If I look forward I win       '
    print(filter_string(text, 'i') + '!')  # 'f  look forward  wn'
    print(filter_string(text, 'O') + '!')  # 'If I lk frward I win
