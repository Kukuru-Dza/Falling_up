#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def has_upper_case(p):
    p1 = p.lower()
    return p != p1





if __name__ == '__main__':
    pass_word = input(str('Enter your password. At least one letter should be capital: '))
    if bool(has_upper_case(pass_word)):
        print('True')
    else:
        print("Not acceptable")

