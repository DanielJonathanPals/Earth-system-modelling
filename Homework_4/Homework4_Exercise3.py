# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 19:11:03 2022

@author: djp99
"""

from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d



rho = 22

u0 = [3,15,1]
t = np.arange(0,40,0.01)

def f(x,t,rho):
    sigma = 10
    beta = 8/3
    return [-sigma*(x[0]-x[1]), rho*x[0]-x[1]-x[0]*x[2], x[0]*x[1]-beta*x[2]]

sol = odeint(f,u0,t,args=(rho,))


#Plot the time series
fig,ax = plt.subplots(3,1, figsize=(7,20))
axis = ['x','y','z']
for i,j in enumerate(axis):
    ax[i].plot(t,sol[:,i])
    ax[i].grid()
    ax[i].set_xlabel('t')
    ax[i].set_ylabel(j)
ax[0].set_title('time series')

#Plot phase portrait
fig2 = plt.figure()
ax2 = plt.axes(projection='3d')
ax2.plot3D(sol[:,0],sol[:,1],sol[:,2])