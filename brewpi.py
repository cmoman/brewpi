#!/usr/bin/env python
#coding:utf-8
# Author:   --<Chris O'Halloran>
# Purpose:  to plot the brewpi data
# Created: 25/06/14

import sys
import unittest

import csv
filename = '/home/cmoman/git/BrewPi/Coopers_Lager.csv'
data = []

try:
    with open(filename) as f:
        #reader = csv.reader(f)
        reader = csv.reader(f, delimiter=';')
        header = reader.next()
        data = [row for row in reader]
except csv.Error as e:
    print "Error reading CSV file at line %s: %s" % (reader.line_num, e)
    sys.exit(-1)

#if header:
    #print header
    #print '=================='
    
a=[]   
b=[]
for datarow in data:
    print datarow
    a.append(datarow[1])
    b.append(datarow[4])
    
import matplotlib
import matplotlib.pyplot as plt

plt.plot(a)
plt.plot(b)
plt.show()