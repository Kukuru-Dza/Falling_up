#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def get_fibonacci_number(a):
    res = []
    if a <= 1:
        return res.append(0)
    if a == 2:
        res = [0, 1]
        return res
    res = [0, 1]
    for i in range(2, a):
        res.append(res[i - 1] + res[i - 2])
    return res


def get_fibonacci_number1(a):
    if a == 1:
        return 0
    if a == 2:
        return 1
    else:
        return get_fibonacci_number1(a - 1) + get_fibonacci_number1((a - 2))


if __name__ == '__main__':
    number = 6
    a = get_fibonacci_number(number)
    print(a)
    print(a[number - 1])
    print()
    b = get_fibonacci_number1(number)
    print(b)

