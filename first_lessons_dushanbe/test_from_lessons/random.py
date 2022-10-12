#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import randint


def choice_from_range(a, b, c):
    random_inx = randint(b, c)
    random_chr = a[random_inx]
    return random_chr


if __name__ == '__main__':
    string = 'qwertyuiop'
    print(choice_from_range(string, 2, 7))