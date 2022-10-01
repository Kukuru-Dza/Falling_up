#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def print_hello(name):
    if isinstance(name, str):
        name1 = name
        print('Hello ' + name1)
    else:
        print('Hello ' + str(name))
    print(name1)


if __name__ == '__main__':
    name = 1234
    print_hello(name)
