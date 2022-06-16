from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np

plt.close('all')
t = np.arange(0,1000,0.1)                                  #Time array for solving the ODE
sigma = 10
beta = 8/3

thrshold = 1                                            #threashold for dicision if trajectory still approaches fixed point
nmbr_of_sctrpnts = 3                                    #numer scatter points plottet for one value of rho

rho_H = sigma*(sigma+beta+3)/(sigma-beta-1)
rho_H_arr = list(np.arange(rho_H-1,rho_H+1,0.1))*nmbr_of_sctrpnts   #list of values for rho in 0.1 steps

def f(x,t,rho):                                         #RHS of Lorenz system
    return [-sigma*(x[0]-x[1]), rho*x[0]-x[1]-x[0]*x[2], x[0]*x[1]-beta*x[2]]

def C_plus_minus(rho):                                       #Calulate the position of C_+ and C_-
    x = np.sqrt(beta*(rho-1))
    y = np.sqrt(beta*(rho-1))
    z = rho-1
    return [np.array([x,y,z]),np.array([-x,-y,z])]

for i,rho in enumerate(rho_H_arr):
    u0 = np.random.randn(3)*0.01                             #random initial conditions close to 0
    tr = odeint(f,u0,t,args=(rho,))                          #Solve ODE
    if np.linalg.norm(tr[-1,:]-C_plus_minus(rho)[0])>thrshold and np.linalg.norm(tr[-1,:]-C_plus_minus(rho)[1])>thrshold:          #Calculate norm of the last point and add to array
        print(f'The estimate for $\\rho_H$ is {rho}')
        print(f'It deviates from the analytic value by {rho-rho_H}')
        break
