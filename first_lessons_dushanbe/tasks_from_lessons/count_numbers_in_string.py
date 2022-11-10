#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' написать функцию подсчета количества каждой цифры в произвольной строке'''


def count(x):
    b = list(x)
    dig_list = []
    for i in range(len(b)):
        if b[i].isdigit():
            dig_list.append(b[i])
    res = [0 for _ in range(10)]
    for k in range(len(dig_list)):
        el = int(dig_list[k])
        res[el] += 1
    return res


if __name__ == '__main__':
    a = 'oiwdoie09 31028u9wr8024978[wd ohcsludgfiwytdajscbow8eyr2 it3riqeyr0qogevj23ri2 uyfpsdjcsl'
    y = count(a)
    for j in range(10):
        if y[j] > 0:
            print(j, ':', y[j], end='; ')
    print()
    print(dict(enumerate(y))) #Словарь
    print(list(enumerate(y))) #Список
    up_zero = lambda x: x > 0
    print(list(filter(up_zero, y)))


