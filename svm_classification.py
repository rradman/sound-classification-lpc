#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 11:11:30 2019

@author: david
"""

import os
import numpy as np
from config import PATH
from sklearn import svm

class SVM_CLF:
    
    zvucni = ['a', 'e', 'i', 'o', 'u',  'j', 'l', 'L', 'r','m',
              'n', 'N','a:', 'e:', 'i:', 'o:', 'u:']
    bezvucni = ['p', 't', 'k', 's', 'S', 'C', 'cc', 'f', 'h', 'c']

    clf = None
    def __init__(self):
        self.clf = svm.SVC(gamma='auto', kernel='rbf', C=1)
     
    def train(self):
        res = []
        clfData = []
        for f in os.listdir("{}/avg".format(PATH)):
            data = np.loadtxt("{}/avg/{}".format(PATH, f))
            f = f.replace(".txt","")
            if f in self.zvucni:
                res.append("z")
                clfData.append(data)
            elif f in self.bezvucni:
                res.append("b")
                clfData.append(data)
        self.clf.fit(clfData, res)

    def predict(self, data):
        if len(data) == 0:
            raise ValueError('data is an empty list')
        elif len(data.shape) == 2:
            data = self.vector_median(data)
        return self.clf.predict([data])
    
    def vector_median(self, data):
        output = []
        data = np.array(data)
        for i in range(13):
            output.append(np.median(data[:,i]))
        return output

