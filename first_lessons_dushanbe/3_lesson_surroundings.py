#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def get_age_difference(y1, y2):
    return (abs(y1-y2))


if __name__ == '__main__':
    year1 = int(input('Enter the year of your birth: '))
    year2 = int(input("Enter the year of your friend's birth: "))
    actual = get_age_difference(year1, year2)
    print('The age difference is ' + str(actual))

