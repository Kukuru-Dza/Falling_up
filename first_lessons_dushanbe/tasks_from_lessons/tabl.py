#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''просто тренировочная таблица умножения на генераторы списков'''

if __name__ == '__main__':
    a = [[0] * 20 for i in range(20)]
    for i in range(20):
        for j in range(20):
            a[i][j] = (i + 1) * (j + 1)

    for i in range(20):
        for j in range(20):
            print("{:4d}".format(a[i][j]), end=' ')
        print()
