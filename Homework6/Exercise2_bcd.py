from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0,2000,0.02)
u0 = [1,1,1]
eps_arr = np.logspace(-1,1,20)

#Define Lorenz System
sigma = 10
beta = 8/3
rho = 28

def lorenz(x,t,rho):   
    return [-sigma*(x[0]-x[1]), rho*x[0]-x[1]-x[0]*x[2], x[0]*x[1]-beta*x[2]]

def C(epsilon,tr,nbr_of_pnts=50):                          #Estimate for C(epsilon)
    if not (isinstance(epsilon, (list,np.ndarray))):
        epsilon = [epsilon]
    max = len(tr)-1
    C_arr = np.zeros(len(epsilon))
    for j,eps in enumerate(epsilon):
        rndm_arr = np.random.randint(int(max/10),max,nbr_of_pnts)
        N_arr = np.zeros(nbr_of_pnts)
        for i,rndm in enumerate(rndm_arr):
            tr_diff = tr-tr[rndm]
            sqr = tr_diff*tr_diff
            norm = 0
            for n,m in enumerate(sqr[0,:]):
                norm += sqr[:,n]
            norm = np.sqrt(norm)
            N_arr[i] = np.count_nonzero(norm<eps)-1
        C_arr[j] = np.sum(N_arr)/nbr_of_pnts/max
    return C_arr

if __name__ == '__main__':
    tr = odeint(lorenz,u0,t,args=(rho,))

    log_eps = np.log(eps_arr)/np.log(10)
    log_C = np.log(C(eps_arr,tr))/np.log(10)

    d,c = np.polyfit(log_eps,log_C,1)
    print(f'The correlation dimension is given by d={round(d,2)}')
    print('''Thus the Lorenz attractor has a correlation dimension close to two.''')

    plt.figure()
    plt.title(f'Correlation dimension of Lorenz attractor (d={round(d,2)})')
    plt.scatter(log_eps,log_C,label='data points',s=8,color='black')
    plt.plot(log_eps,d*log_eps+c,label='Linear regression',color='black')
    plt.xlabel(r'$log_{10}(\varepsilon)$')
    plt.ylabel(r'$log_{10}(C(\varepsilon))$')
    plt.legend()
    plt.show()

    