#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def normalize_url(a):
    if '//' not in a:
        print('https://'+a)
    else:
        while '/' in a:
            a = a.replace(a[0], '')
        print('https://'+a)


if __name__ == '__main__':
    link = 'twitter.com'
    normalize_url(link)
    link = 'https://ya.ru'
    normalize_url(link)
    link = 'http://google.com'
    normalize_url(link)
    link = 'ftp://me.com'
    normalize_url(link)