#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def get_hidden_card(n,a):
    cut = n[-1:(-1-a)]

if __name__ == '__main__':
    card_number=str(input("Enter your card number "))
    a=4
    print ('****' + get_hidden_card(card_number, a))