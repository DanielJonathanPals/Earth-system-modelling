from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

a_arr = np.linspace(2.5,4,500)
x0 = 1e-5

def traj(x0,a,N=500,**kwargs):
    Tr = 0
    if 'Tr' in kwargs.keys(): Tr = kwargs['Tr']
    tr = np.zeros(N)
    tr[0]=x0
    for i in range(N-1):
        tr[i+1] = a*tr[i]*(1-tr[i])
    return tr[Tr:]

def f_prime(x,a):
    return a-2*a*x


if __name__ == '__main__':
    fig,ax = plt.subplots(2,1,sharex=True,figsize=(5,8))
    lyap_arr = np.zeros(len(a_arr))
    for i,a in enumerate(a_arr):
        tr = traj(x0,a,Tr=400)
        lyap_arr[i] = np.sum(np.log(np.abs(f_prime(tr,a))))/len(tr)
        ax[0].scatter(np.ones(len(tr))*a,tr,s=1,color='black')
    ax[1].set_xlabel('a')
    ax[1].axhline(0,color='black',ls='--')
    ax[1].set_ylabel(r'$\lambda$')
    ax[1].plot(a_arr,lyap_arr,color='black')
    ax[1].grid()
    fig.suptitle('Logistic map: Bifurcation diagram')
    plt.show()


