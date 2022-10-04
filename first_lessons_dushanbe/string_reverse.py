#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    string_to_reverse = input(str('Enter a string to be reversed: '))
    string_lenght = len(string_to_reverse)
    remaining_operation = 0
    while remaining_operation < string_lenght:
        print(string_to_reverse[(-1-remaining_operation)], end="")
        remaining_operation = remaining_operation+1
