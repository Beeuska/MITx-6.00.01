# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 08:44:53 2017

@author: MacKenzie Harnett

further test the turtle function. 
"""
import turtle 
bob = turtle.Turtle()

#Exercise 5.6

def Koch(t, x, n):
    if(x<3):
        x.fd(x)
    else:
        for i in range(n):
            for i in range(int(n)):
                t.fd(x/3)
                t.lt(60)
                t.fd(x/3)
                t.lt(-120)
                t.fd(x/3)
                t.lt(60)
                t.fd(x/3)
                t.lt(60)
            t.lt(90)

Koch(bob, 40, 10)
turtle.mainloop()
