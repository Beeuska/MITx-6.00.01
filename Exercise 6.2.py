# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 09:36:07 2017

@author: harne
"""

#Exercise 6.2
def Ackermann(m,n):
    if m==0:
        return n+1
    elif(m>0 and n==0):
        return Ackermann(m-1, 1)
    elif(m>0 and n>0):
        return Ackermann(m-1, Ackermann(m, n-1))
    
print(Ackermann(3, 0))    