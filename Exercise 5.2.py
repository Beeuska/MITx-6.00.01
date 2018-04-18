# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 13:48:37 2017

@author: MacKenzie Harnett
"""
'Exercise 5.2'
'Problem 1'
def check_fermat(a, b, c, n):
    if (n>2):
        if(a**n + b**n == c**n):
            return "Holy smokes, Fermat was wrong!"
    else:
        return "No, that doesn't work"

'Problem 2'
def input_fermat():
    a = int(input("enter a "))
    b = int(input("enter b "))
    c = int(input("enter c "))
    n = int(input("enter n "))
    return check_fermat(a, b, c, n)

print(input_fermat())