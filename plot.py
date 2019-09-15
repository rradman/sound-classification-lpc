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

zvucni = ['a', 'e', 'i', 'o', 'u',  'j', 'l', 'L', 'r','m',
              'n', 'N','a:', 'e:', 'i:', 'o:', 'u:']
bezvucni = ['p', 't', 'k', 's', 'S', 'C', 'cc', 'f', 'h', 'c']

fig = plt.figure()
ax = fig.add_subplot(111,projection="3d")

res = []
clfData = []

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
    else:
        ax.scatter(data[0], data[1], data[2], marker="v", c='y')
        
for f in  os.listdir("{}/avg_Z_B".format(PATH)):
    data = np.loadtxt("{}/avg_Z_B/{}".format(PATH, f))
    ax.scatter(data[0], data[1], data[2], marker="o", c='g')
    
clf = svm.SVC(gamma='auto', kernel='linear', C=1)
clf.fit(clfData, res)

z = lambda x,y: (-clf.intercept_[0]-clf.coef_[0][0]*x-clf.coef_[0][1]*y) / clf.coef_[0][2]

clfData = np.array(clfData)
tmp1 = np.linspace(min(clfData[:,0]),max(clfData[:,0]),100)
tmp = np.linspace(min(clfData[:,1]),max(clfData[:,1]),100)
x,y = np.meshgrid(tmp1,tmp)


ax.plot_surface(x, y, z(x,y),color="k", alpha=0.2)
plt.show()


# primjer za "l" -> zvucni
print(clf.predict([[378.038, -2.0761, 2.14625]]))