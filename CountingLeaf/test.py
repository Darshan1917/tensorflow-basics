# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 16:29:47 2018

@author: dumapath
"""

import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt 




point = np.genfromtxt("point.txt")
data = np.array(point)
#np.random.shuffle(data)
print (data)
colors = 10 *["g","r","c","k"]
# number of clusters 

plt.scatter(data[:,0],data[:,1])
plt.show()

class K_means:
    def __init__ (self,k=2,tol =0.001, max_iter=300):
        self.k = k
        self.tol = tol
        self.max_iter=max_iter
        
    def fit (self , data):
        
        
        self.centroids = {}
        
        
        for i in range(self.k):
            self.centroids[i] = data[i]
            
        for i in range(self.max_iter):
            self.classifications={}
            
            for i in range(self.k):
                self.classifications[i] = []
                
            for featureset in data:
                distances = [np.linalg.norm(featureset-self.centroids[centroid]) for centroid in self.centroids]
                classification = distances.index(min(distances))
                self.classifications[classification].append(featureset)
                
                
            prev_centroids = dict(self.centroids)
            
            for classification in self .classifications:
                #pass
                self.centroids[classification] = np.average(self.classifications[classification] , axis=0)
                
                
            optimized = True
            
            
            for c in self.centroids:
                original_centroid = prev_centroids[c]
                current_centriod = self.centroids[c]
                
                if(np.sum((current_centriod-original_centroid)/ original_centroid *100.0))> self.tol:
                    optimized = False
                    
                if optimized:
                    break
            
            
            
        
    def predict(self,data):
        distances = [np.linalg.norm(data-self.centroids[centroid]) for centroid in self.centroids]
        classification = distances.index(min(distances))
        return classification
    
    
    
    
clf = K_means()
clf.fit(data)




unk = np.array([[5,140],[15,105],[18,125]])



for unks in unk:
    classification = clf.predict(unks)
    plt.scatter(unks[0],unks[1],marker="*", color=colors[classification])

for centroid in clf.centroids:
    plt.scatter(clf.centroids[centroid][0],clf.centroids[centroid][1], marker="o")
    
for classification in clf.classifications:
    color = colors[classification]
    for featureset in clf.classifications[classification]:
        plt.scatter(featureset[0],featureset[1], marker ="x" , color=color)
    