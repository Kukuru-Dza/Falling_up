#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import pi


# a = circle diameter

def circle_square(a=5):
    c_square = (pi * a**2) / 4
    return c_square


def circle_perimeter(a=5):
    c_perim = 2 * pi * (a/2)
    return c_perim

