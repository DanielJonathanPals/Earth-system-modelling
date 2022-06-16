# -*- coding: utf-8 -*-
"""
Created on Wed May 11 14:05:04 2022

@author: Daniel Pals
"""

import numpy as np
from matplotlib import pyplot as plt

C = 1
D = 1
t_max = 6
dt = 0.01
dT0 = [-20,20,-200,200]
T_star = 280



# Part a)

def dT(t,C,D,dT0):
    return dT0*np.exp(-C/D*t)

t = np.arange(0,t_max,dt)

plt.figure(0)
for i in dT0:
    plt.plot(t,dT(t,C,D,i),label=f'dT0 = {i} K')
plt.title(f'Trajectory of dT with C = {C}, D = {D}')
plt.xlabel('time')
plt.ylabel('dT')
plt.legend()
plt.grid()


#Part b)
#Solve the ODE: C*(dT/dt) = (1-alpha)*Q-epsilon*sigma*T**4 = C*(A-B*T**4)

B = D/(4*(T_star**3))
A = T_star**4*B/C
    
x = np.zeros((len(t),len(dT0)))
x[0,:] = np.ones(len(dT0))*T_star + dT0

def f(T):
    return A-B*T**4

for i,j in enumerate(x[:-1,:]):
    x[1+i,:] = j+f(j)*dt
    
    
T_star_array = np.ones(len(t))*T_star

for i in [1,3]:
    plt.figure(i)
    plt.title(f'dT0 = +-{dT0[i]} K, T* = {T_star}, C = {C}, D = {D}')
    plt.plot(t,x[:,i-1],ls='--', label='numeric')
    plt.plot(t,T_star_array+ dT(t,C,D,dT0[i-1]),label='analytic linearized')
    plt.plot(t,x[:,i],ls='--', label='numeric')
    plt.plot(t,T_star_array + dT(t,C,D,dT0[i]),label='analytic linearized')
    plt.xlabel('time')
    plt.ylabel('dT')
    plt.legend()
    plt.grid()





