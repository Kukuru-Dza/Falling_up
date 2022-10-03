#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def trim_and_repeat(t, offset=0, repetitions=1):
    print(t[(-1-(len(t)-offset)):]*repetitions)


if __name__ == '__main__':
    text = 'Namibia'

    trim_and_repeat(text, offset=3, repetitions=2)  # honhon
    trim_and_repeat(text, repetitions=3)  # pythonpythonpython
    trim_and_repeat(text)  # python