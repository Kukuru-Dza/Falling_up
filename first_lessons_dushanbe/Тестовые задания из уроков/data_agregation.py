#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def normalize_url(a):
    if a[:8] == 'https://':
        print(a)
    elif a[:7] == 'http://':
        print('https://'+a[7:])
    else:
        print('https://'+a)


if __name__ == '__main__':

join_numbers_from_range()