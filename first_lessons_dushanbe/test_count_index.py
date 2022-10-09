#!/usr/bin/env python
# -*- coding: utf-8 -*-
from unittest import TestCase
from define_count_and_index import fn_count
from define_count_and_index import fn_index


class LessonArrayTest(TestCase):
    def test_count_item_not_found(self):
        a = [0, 2, 3, 5, 7]
        b = 77
        expected = 0
        got = fn_count(a, b)
        self.assertEqual(got, expected, 'function should return -1 if not found')

    def test_count_item_found(self):
        a = [0, 2, 3, 5, 5, 5, 5, 7]
        b = 5
        expected = 4
        got = fn_count(a, b)
        self.assertEqual(got, expected, f'function should return index ({expected}) but got {got}')

    def test_count_a_is_none(self):
        a = None
        b = 3
        expected = 0
        got = fn_count(a, b)
        self.assertEqual(got, expected, 'function should return 0 if not found')

    def test_count_b_is_none(self):
        a = [0, 2, 3, 5, 7]
        b = None
        expected = 0
        got = fn_count(a, b)
        self.assertEqual(got, expected, 'function should return 0 if not found')

    def test_index_item_not_found(self):
        a = [0, 2, 3, 5, 7]
        b = 77
        expected = False
        got = fn_index(a, b)
        self.assertEqual(got, expected, 'function should return -1 if not found')

    def test_index_item_found(self):
        a = [0, 2, 3, 5, 5, 5, 5, 7]
        b = 3
        expected = 2
        got = fn_index(a, b)
        self.assertEqual(got, expected, f'function should return index ({expected}) but got {got}')

    def test_index_a_is_none(self):
        a = None
        b = 3
        expected = False
        got = fn_index(a, b)
        self.assertEqual(got, expected, 'function should return 0 if not found')

    def test_index_b_is_none(self):
        a = [0, 2, 3, 5, 7]
        b = None
        expected = False
        got = fn_index(a, b)
        self.assertEqual(got, expected, 'function should return 0 if not found')

    def test_index_element_is_string(self):
        a = [1, 3, 'abc', 9]
        b = 'abc'
        expected = 2
        got = fn_index(a, b)
        self.assertEqual(got, expected, f'function should return index ({expected}) but got {got}')

    def test_index_element_is_none(self):
        a = [1, 3, None, 9]
        b = None
        expected = 2
        got = fn_index(a, b)
        self.assertEqual(got, expected, f'function should return index ({expected}) but got {got}')
