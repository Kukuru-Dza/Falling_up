#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''просто тренировочная таблица умножения на генераторы списков'''

if __name__ == '__main__':
    b = 10
    a = [[0]*b for _ in range(b)]
    for i in range(b):
        for j in range(b):
            a[i][j] = (i + 1) * (j + 1)

    for i in range(b):
        for j in range(b):
            print("{:4d}".format(a[i][j]), end=' ')
        print()
