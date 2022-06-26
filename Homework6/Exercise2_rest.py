from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0,100,0.001)
u0 = [1,1,1]
eps_arr = np.logspace(-1,1,20)

#Define Lorenz System
sigma = 10
beta = 8/3
rho = 28

def lorenz(x,t,rho):   
    return [-sigma*(x[0]-x[1]), rho*x[0]-x[1]-x[0]*x[2], x[0]*x[1]-beta*x[2]]

tr = odeint(lorenz,u0,t,args=(rho,))

def C(epsilon,nbr_of_pnts=50):                          #Estimate for C(epsilon)
    if not (isinstance(epsilon, (list,np.ndarray))):
        epsilon = [epsilon]
    max = len(t)-1
    C_arr = np.zeros(len(epsilon))
    for j,eps in enumerate(epsilon):
        rndm_arr = np.random.randint(max/10,max,nbr_of_pnts)
        N_arr = np.zeros(nbr_of_pnts)
        for i,rndm in enumerate(rndm_arr):
            tr_diff = tr-tr[rndm]
            sqr = tr_diff*tr_diff
            norm = np.sqrt(sqr[:,0]+sqr[:,1]+sqr[:,2])
            N_arr[i] = np.count_nonzero(norm<eps)-1
        C_arr[j] = np.sum(N_arr)/nbr_of_pnts
    return C_arr

plt.figure()
plt.plot(eps_arr,C(eps_arr))
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$\varepsilon$')
plt.ylabel(r'$C(\varepsilon)$')
plt.show()

    