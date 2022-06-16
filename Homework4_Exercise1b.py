# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 17:04:59 2022

@author: djp99
"""

from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np

mu = [-2,-1,0,1,2]
u0 = [1,0]
t = np.arange(0,10,0.01)

def f(x,t,mu):
    return [x[1],-x[0]-mu*x[1]]

for i in mu:
    sol = odeint(f,u0,t,args=(i,))
    plt.plot(sol[:,0],sol[:,1], label=f'μ={i}')
    
plt.xlim([-2,2])
plt.ylim([-2,2])
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()