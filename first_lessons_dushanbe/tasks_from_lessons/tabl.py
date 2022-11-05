#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''просто тренировочная таблица умножения на генераторы списков'''

if __name__ == '__main__':
    a = [[0] * 10 for i in range(10)]
    for i in range(10):
        for j in range(10):
            a[i][j] = (i + 1) * (j + 1)

    for i in range(10):
        for j in range(10):
            print("{:3d}".format(a[i][j]), end=' ')
        print()
