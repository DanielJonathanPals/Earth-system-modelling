# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 16:31:55 2022

@author: djp99
"""

import matplotlib.pyplot as plt
import numpy as np

# Exercise 1 a)

μ = np.arange(-3,3,0.1)

#Returns an list with λ plus and minus
def λ(μ):
    if μ**2 < 4:
        return [0.5*(-μ+np.sqrt(4-μ**2)*1j),0.5*(-μ-np.sqrt(4-μ**2)*1j)]
    else:
        return [0.5*(-μ+np.sqrt(μ**2-4)),0.5*(-μ-np.sqrt(μ**2-4))]
  
λ_list = []
for i in μ:
    λ_list.append(λ(i))
λ_list = np.array(λ_list)
    
fig,ax = plt.subplots(3,1, figsize=(7,20))

ax[0].scatter(λ_list[:,0].real,λ_list[:,0].imag, label=r'$\lambda_+$')
ax[0].scatter(λ_list[:,1].real,λ_list[:,1].imag, label=r'$\lambda_-$')
ax[0].legend()
ax[0].grid()
ax[0].set_xlabel('Real Part')
ax[0].set_ylabel('Imaginary Part')

ax[1].plot(μ,λ_list[:,0].real, label=r'$Re(\lambda_+)$')
ax[1].plot(μ,λ_list[:,0].imag, label=r'$Im(\lambda_+)$')
ax[1].legend()
ax[1].grid()
ax[1].set_xlabel('μ')
ax[1].set_ylabel(r'$\lambda_+$')

ax[2].plot(μ,λ_list[:,1].real, label=r'$Re(\lambda_-)$')
ax[2].plot(μ,λ_list[:,1].imag, label=r'$Im(\lambda_-)$')
ax[2].legend()
ax[2].grid()
ax[2].set_xlabel('μ')
ax[2].set_ylabel(r'$\lambda_-$')

    
    
