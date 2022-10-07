#!/usr/bin/env python
# -*- coding: utf-8 -*-
from unittest import TestCase
from lesson_array import find_number
class LessonArrayTest(TestCase):
    def test_index_not_found(self):
        a = [0, 2, 3, 5, 7]
        b = 77
        expected = -1
        got = find_number(a, b)
        self.assertEqual(got, expected, 'function should return -1 if not found')
    def test_index_found(self):
        a = [0, 2, 3, 5, 7]
        b = 5
        expected = 3
        got = find_number(a, b)
        self.assertEqual(got, expected, f'function should return index ({expected}) but got {got}')