#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def get_fibonacci_number(a):
    if a <= 1:
        return 0
    if a == 2:
        return 1
    a1 = 0
    print(a1)
    a2 = 1
    print(a2)
    # count = 3
    # while count <= a:
    #     a3 = a1 + a2
    #     a1 = a2
    #     a2 = a3
    #     count += 1
    for count in range(3, a + 1):
        a3 = a1 + a2
        print(a3)
        a1 = a2
        a2 = a3
    return a3


def get_fibonacci_number1(a):
    if a == 1:
        return 0
    if a == 2:
        return 1
    else:
        return get_fibonacci_number1(a - 1) + get_fibonacci_number1((a-2))


if __name__ == '__main__':
    number = 20
    get_fibonacci_number(number)
    print()
    print(get_fibonacci_number1(number))
