#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def print_hello(n):
    if isinstance(n, str):
        print('Hello, ' + name)
    else:
        print('Hello, ' + str(n))



if __name__ == '__main__':
    name = input('type your name please: ')
    name = name.capitalize()
    print_hello(name)
    name = name.upper()
    print_hello(name)
