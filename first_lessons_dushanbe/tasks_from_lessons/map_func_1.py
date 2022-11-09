#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Write a Python program to find the ration of positive numbers,
negative numbers and zeroes in an array of integers.
'''


def ration(a):
    # ln = len(a)
    c1 = c2 = c3 = 0
    for i in range(len(a)):
        if a[i] < 0:
            c1 += 1
        elif a[i] > 0:
            c2 += 1
        else:
            c3 += 1
    return round(c1/len(a), 2), round(c2/len(a), 2), round(c3/len(a), 2)


if __name__ == '__main__':
    b = [1, -2, 0, 3, -4, 0, 5, -6, -7, 0, 0, 5]
    c1 = list(ration(b))
    print(c1)

