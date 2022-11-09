#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def numgy(a):
    l = [int(i) for i in str(a)]
    if len(l) == 1:
        return a
    else:
        return numgy(sum(l))


if __name__ == '__main__':
    s = 888
    print(numgy(s))
