#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def reverse(a):
    string_lenght = len(a)
    remaining_operation = 0
    reversed_string = ''
    while remaining_operation < string_lenght:
        reversed_string = reversed_string+a[(-1 - remaining_operation)]
        remaining_operation = remaining_operation + 1
    return reversed_string

if __name__ == '__main__':
    string_to_reverse = input(str('Enter a string to be reversed: '))
    print(reverse(string_to_reverse))
