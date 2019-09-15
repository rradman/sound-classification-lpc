#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 13:46:42 2019

@author: david
"""


import tensorflow as tf
from config import PATH
import os
import numpy as np

class NN:
    train_dataset = []
    train_labels = ['z', 'b', 'n']
    train_class = []

    model = None
    def __init__(self):
        os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
        self.model = tf.keras.Sequential([
            tf.keras.layers.Flatten(input_shape=(13,)),
            tf.keras.layers.Dense(128, activation= tf.nn.relu),
            tf.keras.layers.Dense(128, activation= tf.nn.relu),
            tf.keras.layers.Dense(50, activation= tf.nn.relu),
            tf.keras.layers.Dense(3, activation= tf.nn.softmax)
        ])
    
        self.model.compile(optimizer= tf.keras.optimizers.Adam(lr=0.001),
                      loss= 'sparse_categorical_crossentropy',
                      metrics=['accuracy'])

    def train(self):
        zvucni = ['a', 'e', 'i', 'o', 'u',  'j', 'l', 'L', 'r','m',
                      'n', 'N','a:', 'e:', 'i:', 'o:', 'u:']
        bezvucni = ['p', 't', 'k', 's', 'S', 'C', 'cc', 'f', 'h', 'c']

        for f in os.listdir("{}/avg".format(PATH)):
            data = np.loadtxt("{}/avg/{}".format(PATH, f))
            f = f.replace(".txt","")
            self.train_dataset.append(data)
     
            if f in zvucni:   
                self.train_class.append(0)
            elif f in bezvucni: 
                self.train_class.append(1)
            else:
                self.train_class.append(2)

        self.train_labels = np.array(self.train_labels)
        self.train_dataset = np.array(self.train_dataset)

        self.model.fit(self.train_dataset, self.train_class, epochs= 250, 
                       validation_split=0.2, verbose=False)
    
    def predict(self,data):
        if len(data) == 0:
            raise ValueError('data is an empty list')
        elif len(data.shape) == 2:
            data = self.vector_mean(data)
        
        index = np.argmax(self.model.predict(np.array(data).reshape(1,13)))
        return self.train_labels[index]

    def vector_mean(self, data):
        output = []
        data = np.array(data)
        for i in range(13):
            output.append(np.median(data[:,i]))
        return output


