# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 14:09:55 2017

@author: harne
"""
import math
'6.3'
def hypotenuse(x, y):
    '''returns the hypotenuse of 2 sides of a 
    right triangle
    '''
    return math.sqrt(x**2 + y**2)

print(hypotenuse(3, 4))

'6.4'
def is_between(x, y, z):
    if y<=z and y>=x:
        return True
    else:
        return False

print(is_between(4, 6, 7))