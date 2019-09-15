#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 12:51:01 2019

@author: david
"""

from config import PATH
import os

if not os.path.exists("{}/lpc".format(PATH)):
    os.mkdir("{}/lpc".format(PATH))


n = 0
n_len = len(os.listdir(PATH + "/raw/"))

for currentDir in os.listdir("{}/raw/".format(PATH)):
    n += 1
    print("LPC for: {} {} / {}".format(currentDir, n, n_len))

    try:
        os.mkdir("{}/lpc/{}".format(PATH, currentDir))
    except FileExistsError:
#        print("File exists: {}/raw/{}".format(PATH, currentDir))
        pass
    
    length = len(os.listdir("{}/raw/{}".format(PATH, currentDir)))
    counter = 0
    
    for file in os.listdir("{}/raw/{}".format(PATH, currentDir)):
        fullPath = "{}/raw/{}/{}".format(PATH, currentDir, file)
        lpcFile = "{}/lpc/{}/{}".format(PATH, currentDir, file.replace("raw","lpc"))
        
        cmd = "frame -l 320 -p 160 {} | window -l 320 -L 512 | lpc -l 512 -m 12 -f 0.00000001 | x2x +fa13 > {}".format(fullPath, lpcFile)
        os.system(cmd)
        counter +=1
        print("Status: {} %".format(round((counter/length)*100,2)), end="\r", flush=True)
    print("\n", end= "\n")
