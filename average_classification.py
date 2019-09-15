#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 23:18:41 2019

@author: david
"""

from config import PATH
import numpy as np
from scipy.spatial.distance import mahalanobis

def vector_median(data):
    output = []
    data = np.array(data)
    for i in range(13):
        output.append(np.median(data[:,i]))
    return output


def average_classification(data):
    avgZ = np.loadtxt("{}/avg_Z_B/zvucni.txt".format(PATH))
    avgB = np.loadtxt("{}/avg_Z_B/bezvucni.txt".format(PATH))
    
    covarZ = np.loadtxt("{}/covar/zvucni.txt".format(PATH))
    covarB = np.loadtxt("{}/covar/bezvucni.txt".format(PATH))
    
    if len(data) == 0:
        raise ValueError('data is an empty list')
    elif len(data.shape) == 2:
        data = vector_median(data)
        
    
    distZ = mahalanobis(data, avgZ, covarZ)
    distB = mahalanobis(data, avgB, covarB)
    
    #distZ = euclidean(data, avgZ)
    #distB = euclidean(data, avgB)
    
    if distZ < distB:
        return "z"
    else:
        return "b"

