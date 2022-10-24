#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    a = []
    for i in range(3):
        a.append([0] * 3)
    print(a)
    for i in range(3):
        for j in range(3):
            if i == j:
                a[i][j] = 10
            elif i < j:
                a[i][j] = 3
            else:
                a[i][j] = 5
    print(a)
