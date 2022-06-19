# -*- coding: utf-8 -*-
"""
Created on Thu May 26 12:42:42 2022

@author: djp99
"""

from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np

plt.close('all')

#EXERCISE 1:

xMax = 2.5
yMax = 2
DeltaX = 0.5
DeltaY = 1
tMax = 50
DeltaT = 0.01
c = [9,1]


def f(x,t):
    return[x[1],x[0]-x[1]-x[0]**3]

xArray = np.arange(-xMax,xMax+DeltaX,DeltaX)
yArray = np.arange(-yMax,yMax+DeltaY,DeltaY)

plt.figure(1)
for i in xArray:
    for j in yArray:
        t = np.arange(0,tMax,DeltaT)
        sol = odeint(f,[i,j],t)
        plt.plot(sol[:,0],sol[:,1],color='black',lw=1)
        
def V(x,c):
    return np.sqrt(-1/2*x**4+x**2+2*c)

for i in c:
    x_1 = np.arange(-np.sqrt(1+np.sqrt(1+4*i)),np.sqrt(1+np.sqrt(1+4*i)),0.0001)
    x_2 = V(x_1,i)
        
    plt.plot(x_1,x_2,color='red',lw=2,ls='--')
    plt.plot(x_1,-x_2,color='red',lw=2,ls='--')

plt.grid()
plt.xlabel(r'$x_1$')
plt.ylabel(r'$x_2$')
plt.title('orbits')

#EXERCISE 3:
    
xMax = 4
yMax = 3
DeltaX = 0.3
DeltaY = 0.2
tMax = 100
DeltaT = 0.01

def f(x, t):
    return [x[0]*(3-x[0])-2*x[0]*x[1],x[1]*(2-x[1])-x[0]*x[1]]

xArray = np.arange(0,xMax+DeltaX,DeltaX)
yArray = np.arange(0,yMax+DeltaY,DeltaY)

plt.figure(2)
for i in xArray:
    for j in yArray:
        t = np.arange(0,tMax,DeltaT)
        sol = odeint(f,[i,j],t)
        plt.plot(sol[:,0],sol[:,1],color='black',lw=1)
        
plt.grid()
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')
plt.title('orbits')