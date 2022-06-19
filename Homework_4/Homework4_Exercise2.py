# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 17:23:17 2022

@author: djp99
"""


import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fsolve
from scipy.misc import derivative


#(1-0.7+0.4*exp((T-265)/5)/(1+exp((T-265)/5)))*Q vs 0.66*5.67e-8*T^4)


#Right hand side of the ODE; q represents Q/Q_0
def f(T,q):
    Q_0 = 342 #W*m^-2
    sigma = 5.67*10**(-8) #W*m^-2*K^-4
    epsilon = 0.66
    alpha = 0.7-0.4*np.exp((T-265)/5)/(1+np.exp((T-265)/5))
    return (1-alpha)*q*Q_0-epsilon*sigma*T**4

q = np.arange(0.8,1.4,0.005)

fixed_points = {}
for i in q:
    arr = []                                            #This list will be filled with the fixed points of the respective value of q
    for start_value in np.arange(180,300,5):            #Iterrate though inital conditions for the fsolve function in order to find all solutions
        fixed = fsolve(f,start_value,args=(i,))[0]      #returns fixed point
        if abs(f(fixed,i)) < 1:                         #Check that the found fixed point is actually valid
            fixed = round(fixed,1)                      #Round fixed point
            if fixed not in arr and 200 < fixed and 300 > fixed:                        #Check if this fixed point has already been found for some other initial condition
                arr.append(fixed)
    fixed_points[i] = arr                               #Add entry to dictionary
    

stable = []
unstable = []
for key in fixed_points.keys():
    for fp in fixed_points[key]:
        if derivative(f,fp,args=(key,))>0:
            unstable.append([key,fp])
        else:
            stable.append([key,fp])

plt.scatter(np.array(stable)[:,0],np.array(stable)[:,1],color='black',s=5,
            label='stable fixed points')
plt.scatter(np.array(unstable)[:,0],np.array(unstable)[:,1],color='red',s=5,
            label='unstable fixed points')
plt.legend()
plt.grid()
plt.xlabel(r'$Q/Q_0$')
plt.ylabel('T')
plt.title('Bifurcation Diagramm')
