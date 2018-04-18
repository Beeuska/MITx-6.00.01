# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 08:26:52 2017

@author: harne
"""

#Exercise 5.1
import time
time = time.time()

seconds = int(round(time))

minutes = int(time//60)
seconds -= int(minutes*60)
hours = int(minutes//60)
minutes -= int(hours*60)

days = hours//24
hours -= days*24

if(seconds<10):
    print(str(hours)+":"+str(minutes)+":0"+str(seconds))
else:
    print(str(hours)+":"+str(minutes)+":"+str(seconds))

print("It has been " + str(days) + " days since the epoch.")