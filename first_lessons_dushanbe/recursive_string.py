#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def rec_str(a):
    for i in range(0, (len(a) - 1) // 2):
        a[i] = a[i].replace(a[i], a[i] + '(')
        a[-1 - i] = a[-1 - i].replace(a[-1 - i], ')' + a[-1 - i])
    return a

def rec_str_recurs(a):
    if len(a) == 1 or len(a) == 2:
        return a
    else:
        return a[0] + '(' + rec_str_recurs(a[1:-1]) + ')' + a[-1]



if __name__ == '__main__':
    st = input('Enter: ')
    st1 = list(st)
    if len(st1) >= 100:
        res = -1
    else:
        res = ''.join(rec_str(st1))
    print(res)
    print(rec_str_recurs(st))
