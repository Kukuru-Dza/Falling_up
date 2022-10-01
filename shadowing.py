#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def truncate(t, n):
    return t[:n] + '...'


if __name__ == '__main__':
    text = input("input text: ")
    number = int(input("input number: "))
    print(truncate(text, number))
    print(text, number)

    text_for_print = input("input text: ")
    symbol_qty = int(input("input number: "))
    print(truncate(text_for_print, symbol_qty))