from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
import Exercise3_ab as ex3ab
import Exercise2_bcd as ex2bcd

a = 3.5699456
x0 = 1e-5
N = 20000
eps_arr = np.logspace(-1,-0.4,20)

tr = ex3ab.traj(x0,a,N,Tr=2000)
tr = tr.reshape(len(tr),1)
log_C = np.log(ex2bcd.C(eps_arr,tr,200))/np.log(10)
log_eps = np.log(eps_arr)/np.log(10)

d,c = np.polyfit(log_eps,log_C,1)
print(f'The correlation dimension is given by d={round(d,2)}')

plt.figure()
plt.title(f'Correlation dimension of Lorenz attractor (d={round(d,2)})')
plt.scatter(log_eps,log_C,label='data points',s=8,color='black')
plt.plot(log_eps,d*log_eps+c,label='Linear regression',color='black')
plt.xlabel(r'$log_{10}(\varepsilon)$')
plt.ylabel(r'$log_{10}(C(\varepsilon))$')
plt.legend()
plt.show()