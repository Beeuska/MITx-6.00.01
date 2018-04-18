# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 14:06:47 2017

@author: MacKenzie Harnett

Simple recursive practice
"""

'Exercise 5.4'
def recurse(n, s):
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)
recurse(3, 0)
'Problem 1'
recurse(-1, 0)
