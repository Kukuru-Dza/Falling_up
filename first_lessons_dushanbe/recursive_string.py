#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def rec_str(a):
    for i in range(0, (len(a) - 1) // 2):
        a[i] = a[i].replace(a[i], a[i] + '(')
        a[-1 - i] = a[-1 - i].replace(a[-1 - i], ')' + a[-1 - i])
    return a

def rec_str_recurs(a):



if __name__ == '__main__':
    st = list(input('Enter: '))
    if len(st) >= 100:
        res = -1
    else:
        res = ''.join(rec_str(st))
    print(res)
