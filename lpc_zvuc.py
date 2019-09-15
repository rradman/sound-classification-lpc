#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 15:39:48 2019

@author: david
"""

import os
from config import PATH
import numpy as np

if not os.path.exists("{}/avg_Z_B".format(PATH)):
    os.mkdir("{}/avg_Z_B".format(PATH))

if not os.path.exists("{}/covar".format(PATH)):
    os.mkdir("{}/covar".format(PATH))

zvucni = ['a', 'e', 'i', 'o', 'u',  'j', 'l', 'L', 'r','m',
              'n', 'N','a:', 'e:', 'i:', 'o:', 'u:']
bezvucni = ['p', 't', 'k', 's', 'S', 'C', 'cc', 'f', 'h', 'c']


dataZ = []
dataB = []

for currentLetter in os.listdir("{}/avg".format(PATH)):
    letter = currentLetter.replace(".txt","")
    data = np.loadtxt("{}/avg/{}".format(PATH,currentLetter))
    
    if letter in zvucni:
        dataZ.append(data)
    elif letter in bezvucni:
        dataB.append(data)

meanZ = []
dataZ = np.array(dataZ)
for i in range(13):
    meanZ.append(np.median(dataZ[:,i]))

np.savetxt("{}/avg_Z_B/zvucni.txt".format(PATH), meanZ)

np.savetxt("{}/zvucniData.lpc".format(PATH), dataZ)
os.system("vstat -l 13 -o 2 -i {}/zvucniData.lpc | x2x +fa13 > {}/covar/zvucni.txt".format(PATH,PATH))
os.system("rm {}/zvucniData.lpc".format(PATH))

meanB = []
dataB = np.array(dataB)
for i in range(13):
    meanB.append(np.median(dataB[:,i]))
np.savetxt("{}/avg_Z_B/bezvucni.txt".format(PATH), meanB)

np.savetxt("{}/bezvucniData.lpc".format(PATH), dataB)
os.system("vstat -l 13 -o 2 -i {}/bezvucniData.lpc | x2x +fa13 > {}/covar/bezvucni.txt".format(PATH,PATH))
os.system("rm {}/bezvucniData.lpc".format(PATH))
    



