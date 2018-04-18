# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 08:39:21 2017

@author: harne
"""
import turtle 
bob = turtle.Turtle()
#Exercise 5.5

def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    t.fd(length*n)
    t.lt(angle)
    draw(t, length, n-1)
    t.rt(2*angle)
    draw(t, length, n-1)
    t.lt(angle)
    t.bk(length*n)

draw(bob, 10, 10)
turtle.mainloop()