#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def filter_string (a, b):
    output_string = ''
    if a[0] == ' ':
        a = a[1:]
    if a[-1] == ' ':
        a = a[:-1]
    count = 0
    for symbol in a:
        if b.lower() != a[count].lower():
            output_string += a[count]
        count += 1
    return output_string


if __name__ == '__main__':
    text = ' If I look forward I win '
    print(filter_string(text, 'i') + '!')  # 'f  look forward  wn'
    print(filter_string(text, 'O') + '!')  # 'If I lk frward I win
