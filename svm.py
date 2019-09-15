#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 16:04:59 2019

@author: david
"""
from mpl_toolkits.mplot3d import  Axes3D
import matplotlib.pyplot as plt

import os
import numpy as np
from config import PATH
from sklearn import svm


fig = plt.figure()
ax = fig.add_subplot(111,projection="3d")

zvucni = ['a', 'e', 'i', 'o', 'u',  'j', 'l', 'L', 'r','m',
              'n', 'N','a:', 'e:', 'i:', 'o:', 'u:']
bezvucni = ['p', 't', 'k', 's', 'S', 'C', 'cc', 'f', 'h', 'c']

res = []
clfData = []

testres = []
testData = []

for f in os.listdir("{}/avg".format(PATH)):
    data = np.loadtxt("{}/avg/{}".format(PATH, f))
    f = f.replace(".txt","")
    
    if f in zvucni:
        ax.scatter(data[0], data[1], data[2], marker='*', c='b')
        res.append("zvucni")
        clfData.append(data[:3])
    elif f in bezvucni:
        ax.scatter(data[0], data[1], data[2], marker="+", c='r')
        res.append("bezvucni")
        clfData.append(data[:3])        

clf = svm.SVC(gamma='scale', kernel='linear', C=1, decision_function_shape='ovo')
clf.fit(clfData, res)


ax.scatter(184.71333333333334, -1.3873033333333333, 1.000425,c= 'g')

# primjer za "l" -> zvucni
print(clf.predict([[597.234,	-1.62961,	1.67207]]))


# primjer za "b" -> nedefinirano
print(clf.predict([[184.71333333333334, -1.3873033333333333, 1.000425]]))

print(clf.predict([[1.695365796363824984e+02, -1.469186846164510118e+00, 8.688537186392194522e-01]]))

