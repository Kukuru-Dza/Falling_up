#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def pascal_tr(b):
    a = []
    for i in range(b + 1):
        a.append([1] + [0] * b)

    for i in range(1, (b + 1)):
        for j in range(1, (i + 1)):
            a[i][j] = a[i - 1][j - 1] + a[i - 1][j]
    return a[b]


if __name__ == '__main__':
    a = 10
    print(pascal_tr(a))
