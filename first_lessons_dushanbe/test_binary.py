#!/usr/bin/env python
# -*- coding: utf-8 -*-
from unittest import TestCase
from array_sorting_binary_search import bin_index
from array_sorting_bubbles import list_sort


# NOT READY  YET!!!!!!!!!!!!!!!


class ArrayTest(TestCase):

    def test_list_correct(self):
        a = [-4, 6, 3, 7, 22, 1, 1, 1, -1]
        expected = [-4, -1, 1, 1, 1, 3, 6, 7, 22]
        got = list_sort(a)
        self.assertEqual(got, expected, f'function should return index ({expected}) but got {got}')

    def test_list_none(self):
        a = None
        expected = a
        got = list_sort(a)
        self.assertEqual(got, expected, f'function should return index ({expected}) but got {got}')
