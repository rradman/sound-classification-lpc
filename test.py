# -*- coding: utf-8 -*-
import numpy as np
from sklearn.neural_network import MLPClassifier 
import os
from config import PATH


# promijeniti a_ e_ i_ i_ u_
zvucni = ['a', 'e', 'i', 'o', 'u',  'j', 'l', 'L', 'r','m',
              'n', 'N','a_', 'e_', 'i_', 'o_', 'u_']
bezvucni = ['p', 't', 'k', 's', 'S', 'C', 'cc', 'f', 'h', 'c']

Y = []  
glasovi = []

for f in os.listdir("{}/avg".format(PATH)):
    data = np.loadtxt("{}/avg/{}".format(PATH, f))
    f = f.replace(".txt","")
    glasovi.append(data)
    if f in zvucni:
        Y.append('zvucni')
    elif f in bezvucni:
        Y.append('bezvucni')
    else:
        Y.append('nedefinirano')

glasovi = np.array(glasovi)

#parametri modela
hidden_layer_sizes = [(5,), (10,10), (30,30,30)]
activation = ["logistic", "identity", "tanh"]
solver = ["sgd", "adam"]
alpha = [0.0001, 0.00001]

#izrada modela
clf = MLPClassifier(hidden_layer_sizes = hidden_layer_sizes[0],\
                    activation = activation[0],\
                    max_iter = 10000,\
                    solver = solver[1],\
                    alpha = alpha[0])

#Treniranje/Učenje klasifikatora s podacima za treniranje 
clf.fit(glasovi,Y)

######################### TESTIRANJE ##################
### mijenjati varijablu "glas"
countz = 0
countb = 0
countn = 0
for i in range(500):
    glas = "b"
    test = []
    test2 = []  
    duljina = len(os.listdir("{}/lpc/{}".format(PATH, glas)))
    radnom_choice = int(np.random.rand() * duljina)
    test = np.loadtxt("{}/lpc/{}/{}+.lpc".format(PATH, glas, radnom_choice))
    
    for i in range(len(test[0])):
        test2.append(np.mean(test[:,i])) 
       
    test = np.array(test2)
    A = np.reshape(test, (-1, 1))
    A = A.T
    predict = clf.predict(A)
    #print ("\nPredikcija:\n\n" + str(predict))
    if predict == "zvucni":
        countz += 1
    elif predict == "bezvucni":
        countb += 1
    else:
        countn += 1 
print(countz,countb,countn)
print("Postotci: ", countz/500,countb/500,countn/500)
        
    










