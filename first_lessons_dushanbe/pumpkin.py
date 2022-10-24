#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == "__main__":
    word = 'pumkin'
    count = 0
    for one in word:
        for two in word:
            for three in word:
                for four in word:
                    for five in word:
                        for six in word:
                            res = (one+two+three+four+five+six)
                            if res[0] in 'pmkn' and res[-1] in 'pmkn':
                                if res.count('u')+res.count('i'):
                                    count += 1
    print(count)