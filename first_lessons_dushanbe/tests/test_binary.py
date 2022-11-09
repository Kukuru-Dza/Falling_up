#!/usr/bin/env python
# -*- coding: utf-8 -*-
from unittest import TestCase
from binary_search import bin_index


class ArrayTest(TestCase):

    def test_search_correct_odd(self):
        a = [1, 2, 3, 4, 8, 17, 22]
        b = 4
        expected = 3
        got = bin_index(a, b)
        self.assertEqual(got, expected, f'function should return index ({expected}) but got {got}')

    def test_search_correct_even(self):
        a = [1, 2, 3, 4, 8, 17]
        b = 4
        expected = 3
        got = bin_index(a, b)
        self.assertEqual(got, expected, f'function should return index ({expected}) but got {got}')

    def test_search_not_in_list(self):
        a = [1, 2, 3, 4, 8, 17, 22]
        b = 5
        expected = -1
        got = bin_index(a, b)
        self.assertEqual(got, expected, f'function should return index ({expected}) but got {got}')

    def test_search_less_than_min(self):
        a = [1, 2, 3, 4, 8, 17, 22]
        b = 0
        expected = -1
        got = bin_index(a, b)
        self.assertEqual(got, expected, f'function should return index ({expected}) but got {got}')

    def test_search_more_than_max(self):
        a = [1, 2, 3, 4, 8, 17, 22]
        b = 23
        expected = -1
        got = bin_index(a, b)
        self.assertEqual(got, expected, f'function should return index ({expected}) but got {got}')

    def test_search_a_none(self):
        a = None
        b = 4
        expected = -1
        got = bin_index(a, b)
        self.assertEqual(got, expected, f'function should return index ({expected}) but got {got}')

    def test_search_b_none(self):
        a = [1, 2, 3, 4, 8, 17, 22]
        b = None
        expected = -1
        got = bin_index(a, b)
        self.assertEqual(got, expected, f'function should return index ({expected}) but got {got}')