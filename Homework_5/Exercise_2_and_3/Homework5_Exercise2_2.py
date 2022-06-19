import matplotlib.pyplot as plt
import numpy as np
import Homework5_usefull_fcts as usfll

rho_list = np.random.rand(50)*(usfll.rho_H-1)+1                 #Chose some random positive values of rho in the Intervall [1,rho_H]
t = np.arange(0,100,0.1)                                        #Timespan over which the trajectory is computed

init_pnts = np.zeros((len(rho_list),3))                         #Randomly choose whether to start close to C_+ or C_-
for i in range(len(init_pnts)):
    init_pnts[i,:] = usfll.C_plus_minus(rho_list[i])[np.random.randint(0,2)]

data = usfll.create_data(rho_list,t,3,init_pnts)                #Random initial conditions

fig,ax = plt.subplots(3,1,sharex=True,figsize=(5,8))                                  #plot results
fig.suptitle(r'Conv. of traj. starting close to $C_+$ and $C_-$')
ylabels = ['x','y','z']
x = np.arange(1,usfll.rho_H,0.1)
for i,curr_ax in enumerate(ax):
    curr_ax.plot(x,usfll.C_plus_minus(x)[0][i],color='gray',ls='-',label=r'$C_+$')
    curr_ax.plot(x,usfll.C_plus_minus(x)[1][i],color='gray',ls='--',label=r'$C_-$')
    curr_ax.scatter(data[:,0],data[:,1+i],color='gray',s=8,label='initial point')
    curr_ax.scatter(data[:,0],data[:,4+i],color='black',s=30,label='final point')
    curr_ax.grid()
    curr_ax.set_xlabel(r'$\rho$')
    curr_ax.set_ylabel(ylabels[i])

ax[2].legend()
plt.tight_layout()
plt.show()