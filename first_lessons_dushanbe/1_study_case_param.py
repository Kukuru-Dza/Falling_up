#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def get_hidden_card(n,a):
    print(("*"*a) + n[-5:-1])


if __name__ == '__main__':
    a = 2
    card_number=str(input("Enter your card number "))
    if len(card_number)==16:
        get_hidden_card(card_number, a)
    else:
        print('Incorrect card number')
        card_number = str(input("Enter your card number "))
        get_hidden_card(card_number, a)
