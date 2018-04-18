# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 13:58:54 2017

@author: MacKenzie Harnett
Tests whether or not an object is a triangle. 
"""

'Exerise 5.3'
'Problem 1'
def is_triangle(a, b, c):
    if(a>b+c or b>a+c or c>a+b):
        return "\nNo"
    return "\nYes"

'Problem 2'
def input_triangle():
    a = int(input("enter a "))
    b = int(input("enter b "))
    c = int(input("enter c "))
    return is_triangle(a, b, c)

print(input_triangle())
