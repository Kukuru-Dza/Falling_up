#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def fact(a):
#     r = 1
#     for i in range(2, a+1):
#         r *= i
#     return r
    if a == 1:
        return 1
    else:
        return fact(a-1)*a


if __name__ == '__main__':
    print(fact(5))
