#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def join_numbers_from_range(a, b):
    string = ''
    while a <= b:
        string = string+str(a)
        a = a+1
    return string


if __name__ == '__main__':
    print(join_numbers_from_range(3, 15))