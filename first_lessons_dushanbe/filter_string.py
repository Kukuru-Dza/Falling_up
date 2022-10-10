#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def filter_string(a, b):
    if a is None:
        return False
    output_string = ''
    while a[0] == ' ':
        a = a[1:]
    while a[-1] == ' ':
        a = a[:-1]
    if b is None:
        return a
    count = 0
    for _ in a:
        if b.lower() != a[count].lower():
            output_string += a[count]
        count += 1
    return output_string


if __name__ == '__main__':
    text = '       If I look forward I win       '
    print(filter_string(text, 'i') + '!')  # 'f  look forward  wn'
    print(filter_string(text, 'O') + '!')  # 'If I lk frward I win
