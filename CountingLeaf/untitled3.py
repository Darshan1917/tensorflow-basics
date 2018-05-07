# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 18:53:58 2018

@author: dumapath
"""

import numpy as np
import matplotlib.pyplot as plt

X = np.array([1,2,3,4,5,6,7])
Y = np.array([11,12,13,14,15,16,17])
print(X)
dit = [None]*len(X)
print(len(dit))

plt.plot(X,Y)

class NeareatNeighbour:
    def __init__(self):
        pass
    
    def train(self,X,Y):
        self.X = X
        self.Y = Y
        
    def predict(self,X_new):
        num_test = X.shape[0]
        Ypred = np.zeros(num_test)
        
        for i in range(num_test):
            dit[i] = np.sum(np.abs(self.X[i] - X_new))
        print(dit)
            #value = np.array([dist])
            #print (value)
        min_index = np.argmin(np.array(dit))
        print(min_index)
        #print(min_index)
        Ypred[i] = self.Y[min_index]
        #print(Ypred)
        return Ypred
    
    
X_new  = np.array([3])  
val = NeareatNeighbour()
fit = val.train(X,Y)
result = val.predict(X_new)
print(result)
        
    
    
    