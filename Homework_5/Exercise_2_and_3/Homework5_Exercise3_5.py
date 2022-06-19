import matplotlib.pyplot as plt
import numpy as np
import Homework5_usefull_fcts as usfll

rho_list = np.random.randn(30)*1.5+usfll.rho_H                  #Chose some random values for rho close to rho_H
t = np.arange(0,300,0.1)                                        #Timespan over which the trajectory is computed

init_pnts = np.zeros((len(rho_list),3))                         #Set initial conditions to C_+
for i in range(len(init_pnts)):
    init_pnts[i,:] = usfll.C_plus_minus(rho_list[i])[0]

data = usfll.create_data(rho_list,t,dist=0.3,init_pnt=init_pnts)    #random initial conditions close to C_+

fig,ax = plt.subplots(3,1,sharex=True,figsize=(5,8))                                      #plot results
fig.suptitle(r'Change of conv. for traj. starting close to $C_+$')
x = np.linspace(np.min(rho_list),np.max(rho_list),100)
ylabels = ['x','y','z']
for i,curr_ax in enumerate(ax):
    curr_ax.plot(x,usfll.C_plus_minus(x)[0][i],color='gray',ls='-',label=r'$C_+$')
    curr_ax.scatter(data[:,0],data[:,1+i],color='gray',s=8,label='initial point')
    curr_ax.scatter(data[:,0],data[:,4+i],color='black',s=30,label='final point')
    curr_ax.grid()
    curr_ax.set_xlabel(r'$\rho$')
    curr_ax.set_ylabel(ylabels[i])
    curr_ax.axvline(usfll.rho_H,color='red',ls='--',label=r'$\rho_H$')

ax[2].legend()
plt.tight_layout()
plt.show()
