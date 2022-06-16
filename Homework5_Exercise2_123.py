from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np

plt.close('all')
t = np.arange(0,100,1)                                  #Time array for solving the ODE
sigma = 10
beta = 8/3

nmbr_of_sctrpnts = 3                                    #numer scatter points plottet for one value of rho

rho_H = sigma*(sigma+beta+3)/(sigma-beta-1)
rho_H_arr = list(np.linspace(0,rho_H+10,50))*nmbr_of_sctrpnts   #list of values for rho

def f(x,t,rho):                                         #RHS of Lorenz system
    return [-sigma*(x[0]-x[1]), rho*x[0]-x[1]-x[0]*x[2], x[0]*x[1]-beta*x[2]]

def fp_norm(rho):                                       #Calulate analytic norm for 1<rho<rho_H
    x = np.sqrt(beta*(rho-1))
    y = np.sqrt(beta*(rho-1))
    z = rho-1
    return np.sqrt(x**2+y**2+z**2)

norm_arr = np.zeros(len(rho_H_arr))                     #Initialize array for collecting data points
for i,rho in enumerate(rho_H_arr):
    u0 = np.random.randn(3)*0.01                        #random initial conditions close to 0
    tr = odeint(f,u0,t,args=(rho,))                     #Solve ODE
    norm_arr[i] = np.linalg.norm(tr[-1,:])              #Calculate norm of the last point and add to array

rho = np.arange(1,rho_H+10,0.1)                            #plot analytic result
plt.plot(rho,fp_norm(rho),color='green',label='analytic solution')

plt.scatter(rho_H_arr,norm_arr,s=8,color='black')
plt.grid()
plt.title('Stable fixed points of Lorenz system')
plt.xlabel(r'$\rho_H$')
plt.ylabel(r'$\lim_{t \to \infty} \; ||\vec{x}||$')
plt.axvline(1,color='red',ls='--')
plt.axvline(rho_H,color='red',ls='--')
plt.legend(loc='best')
plt.show()