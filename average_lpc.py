#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 13:47:35 2019

@author: david
"""

from config import PATH
import os
import numpy as np

if not os.path.exists("{}/avg".format(PATH)):
    os.mkdir("{}/avg".format(PATH))

n = 0
n_len = len(os.listdir(PATH + "/lpc/"))

for currentDir in os.listdir("{}/lpc".format(PATH)):    
    n += 1
    print("Average LPC for: {} {} / {}".format(currentDir, n, n_len))
    
    
    data = []
    for file in os.listdir("{}/lpc/{}".format(PATH,currentDir)):
        for i in np.loadtxt("{}/lpc/{}/{}".format(PATH,currentDir,file)):
            data.append(i)
    
    output = []
    data = np.array(data)
    for i in range(13):
        output.append(np.median(data[:,i]))
        
    np.savetxt("{}/avg/{}.txt".format(PATH,currentDir), output)
