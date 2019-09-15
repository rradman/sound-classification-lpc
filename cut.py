#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 18:41:08 2019

@author: david
"""
from scipy.io import wavfile
from os import listdir, makedirs, path
import math


for c in listdir('lab'):    
    with open("lab/" + c,"r") as f: 
        try:
            rate, data = wavfile.read("wav/" + c.replace(".lab",".wav"))
            for l in f.readlines():
                l = l.split()
        
                start = int(l[0])
                end = int(l[1])
                voice = l[2]
    
                duration = (end-start)* math.pow(10,-7)
                duration = duration * rate
                duration = math.ceil(duration)
            
                d = "sounds/" + l[2]    
                if not path.exists(d):
                    makedirs(d)

        
                name = "sounds/{}/{}.wav".format(voice,len(listdir(d)))
                wavfile.write(name,rate,data[:duration])
                data = data[duration:]
         
        except FileNotFoundError:
            pass
     