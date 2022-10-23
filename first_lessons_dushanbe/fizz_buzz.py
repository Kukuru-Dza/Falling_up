#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Если число делится без остатка на 3, то вместо него выводится слово Fizz
#Если число делится без остатка на 5, то вместо него выводится слово Buzz
#Если число делится без остатка и на 3, и на 5, то вместо числа выводится слово FizzBuzz
#В остальных случаях в строку добавляется само число
def fizz_buzz(a, b):
    if a > b or a is None or b is None:
        return ''
    for i in range(a, b+1):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz', end=' ')
        elif i % 3 == 0 and i % 5 != 0:
            print('Fizz', end=' ')
        elif i % 3 != 0 and i % 5 == 0:
            print('Buzz', end=' ')
        else:
            print(i, end=' ')


if __name__ == '__main__':
    print(fizz_buzz(1, 6))
