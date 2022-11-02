#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def rew(a):
    if len(a) == 1 and a[0] != '(':
        return a
    elif len(a) == 1 and a[0] == '(':
        return ')'
    else:
        if a[-1] == '(':
            return ')' + rew(a[:-1])
        else:
            return a[-1] + rew(a[:-1])


if __name__ == '__main__':
    s = '(((t((p((y((kx((((e(((((((vw((v(e((v(m((('
    print(s + rew(s))
