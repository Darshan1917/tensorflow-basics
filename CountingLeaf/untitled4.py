from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

import pandas as pd
import numpy as np
import random


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

point = np.genfromtxt("points.txt")
data = np.array(point)
print(data[4])


ax.scatter(data[0],data[1], data[2], c='r', marker='o')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()