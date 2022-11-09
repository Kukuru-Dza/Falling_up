#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' написать функцию подсчета количества каждой цифры в произвольной строке'''


def count(x):
    res = [0 for ii in range(10)]
    for k in range(len(x)):
        el = int(x[k])
        res[el] += 1
    return res


if __name__ == '__main__':
    a = 'oiwdoie09 31028u9wr8024978[wd ohcsludgfiwytdajscbow8eyr2 it3riqeyr0qogevj23ri2 uyfpsdjcsl'
    b = list(a)
    dig_list = []
    for i in range(len(b)):
        if b[i].isdigit():
            dig_list.append(b[i])
    y = count(dig_list)
    for i in range(10):
        if y[i] > 0:
            print(i, ':', y[i], end='; ')
    print()
    print(dict(enumerate(y))) #Словарь
    print(list(enumerate(y))) #Список
    up_zero = lambda x: x > 0
    print(list(filter(up_zero, y)))


