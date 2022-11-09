#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Если число делится без остатка на 3, то вместо него выводится слово Fizz
# Если число делится без остатка на 5, то вместо него выводится слово Buzz
# Если число делится без остатка и на 3, и на 5, то вместо числа выводится слово FizzBuzz
# В остальных случаях в строку добавляется само число
def fizz_buzz(a, b):
    out_str = []
    if a > b or a is None or b is None:
        return ''
    for i in range(a, b + 1):
        if i % 3 == 0 and i % 5 == 0:
            out_str.append('FizzBuzz')
        elif i % 3 == 0 and i % 5 != 0:
            out_str.append('Fizz')
        elif i % 3 != 0 and i % 5 == 0:
            out_str.append('Buzz')
        else:
            out_str.append(i)
    return out_str


if __name__ == '__main__':
    start = 2
    end = 22
    x = fizz_buzz(start, end)
    print(x)
    for i in x:
        print(i, end=' ')
