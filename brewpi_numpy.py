#!/usr/bin/env python
#coding:utf-8
# Author:   --<>
# Purpose: 
# Created: 29/06/14

import sys
import unittest

import matplotlib
import matplotlib.pyplot as plt

import numpy

def tofloat(s):
    try:
        p = float(s)
    except:
        p=0.0
    return p

def import_the_file2():

    c, v = numpy.loadtxt('Coopers_Lager.csv', delimiter=';' , usecols=(1,4), unpack=True, converters={1:tofloat, 4:tofloat})
    
    plt.plot(c)
    plt.plot(v)
    
    plt.show()

if __name__=='__main__':
    import_the_file2()