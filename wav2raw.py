#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 23:00:26 2019

@author: david
"""
from config import PATH
import os
n = 0
n_len = len(os.listdir(PATH + "/glasovi/"))
for currentDir in os.listdir(PATH + "/glasovi/"):
    n += 1
    print("Current letter: {} {} / {}".format(currentDir, n, n_len))
    
    try:
        os.mkdir("{}/raw/{}".format(PATH, currentDir))
    except FileExistsError:
        #print("File exists: {}/raw/{}".format(PATH, currentDir))
        pass
    
    length = len(os.listdir("{}/glasovi/{}".format(PATH, currentDir)))
    counter = 0
    for file in os.listdir("{}/glasovi/{}".format(PATH, currentDir)):
        fullPath = "{}/glasovi/{}/{}".format(PATH, currentDir, file)
        rawFile = "{}/raw/{}/{}".format(PATH, currentDir, file.replace("wav","raw"))
 
        os.system("sox {} -e signed-integer -t raw {}".format(fullPath, rawFile))
        os.system("x2x +sf {} > {}".format(rawFile, rawFile.replace(".raw", "+.raw")))
        os.remove(rawFile)
        
        counter +=1
        print("Status: {} %".format(round((counter/length)*100,2)), end="\r", flush=True)
    print("\n", end= "\n")