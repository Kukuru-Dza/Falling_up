#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def string_or_not(a):
    return isinstance(a, str)

if __name__ == '__main__':
    print(string_or_not(12))