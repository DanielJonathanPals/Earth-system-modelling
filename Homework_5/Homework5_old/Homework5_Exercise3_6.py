from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np

plt.close('all')
t = np.arange(0,300,1)                                  #Time array for solving the ODE
sigma = 10
beta = 8/3

nmbr_of_sctrpnts = 50                                    #numer scatter points plottet for one value of rho

rho_H = sigma*(sigma+beta+3)/(sigma-beta-1)
rho = rho_H-0.1

def f(x,t,rho):                                         #RHS of Lorenz system
    return [-sigma*(x[0]-x[1]), rho*x[0]-x[1]-x[0]*x[2], x[0]*x[1]-beta*x[2]]

def C_plus_minus(rho):                                       #Calulate the position of C_+ and C_-
    x = np.sqrt(beta*(rho-1))
    y = np.sqrt(beta*(rho-1))
    z = rho-1
    return [np.array([x,y,z]),np.array([-x,-y,z])]

def fp_norm(rho):                                       #Calulate analytic norm for 1<rho<rho_H
    x = np.sqrt(beta*(rho-1))
    y = np.sqrt(beta*(rho-1))
    z = rho-1
    return np.sqrt(x**2+y**2+z**2)

init_norm = np.zeros(nmbr_of_sctrpnts)
final_norm = np.zeros(nmbr_of_sctrpnts)
for i in range(nmbr_of_sctrpnts):
    u0 = np.random.randn(3)*1.5+C_plus_minus(rho)[0]   #random initial conditions close to 0
    tr = odeint(f,u0,t,args=(rho,))                     #Solve ODE
    init_norm[i] = np.linalg.norm(tr[0,:]-C_plus_minus(rho)[0])              #Calculate norm of the last point and add to array
    final_norm[i] = np.linalg.norm(tr[-1,:]-C_plus_minus(rho)[0])

plt.scatter(init_norm,final_norm)
plt.show()