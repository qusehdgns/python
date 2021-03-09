# 2021/03/09
import numpy as np
import matplotlib.pyplot as plt
from sklearn import *
import sklearn

time = np.array([1,2,3,4],dtype = int)
score = np.array([70,80,95,90],dtype = int)

fig = plt.figure()
fig, ax = plt.subplots(1, 1, figsize=(8,4) , constrained_layout=True)
ax.plot( time, score, label = "", c = None )
ax.set_title("")
ax.set_xlabel("")
ax.set_ylabel("")
ax.legend(loc='best')
ax.scatter( time, score, label = "", c = 'red' )
ax.set_title("time_score")
ax.set_xlabel("time")
ax.set_ylabel("score")
ax.legend(loc='best')
plt.show()

model = sklearn.linear_model.LinearRegression()
model.fit(time,score)