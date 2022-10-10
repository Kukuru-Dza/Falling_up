#!/usr/bin/env python
# -*- coding: utf-8 -*-
from unittest import TestCase
from filter_string import filter_string


class LessonArrayTest(TestCase):
    def test_filter_item_found(self):
        text = '       If I look forward I win       '
        symbol = 'I'
        expected = 'f  look forward  wn'
        got = filter_string(text, symbol)
        self.assertEqual(got, expected, f'function should return ({expected}) but got {got}')

    def test_filter_item_found(self):
        text = '       If I look forward I win       '
        symbol = 'i'
        expected = 'f  look forward  wn'
        got = filter_string(text, symbol)
        self.assertEqual(got, expected, f'function should return ({expected}) but got {got}')

    def test_filter_text_none(self):
        text = None
        symbol = 'I'
        expected = False
        got = filter_string(text, symbol)
        self.assertEqual(got, expected, f'function should return ({expected}) but got {got}')

    def test_filter_symbol_none(self):
        text = '       If I look forward I win       '
        symbol = None
        expected = 'If I look forward I win'
        got = filter_string(text, symbol)
        self.assertEqual(got, expected, f'function should return ({expected}) but got {got}')