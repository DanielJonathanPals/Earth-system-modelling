import matplotlib.pyplot as plt
import numpy as np
import Homework5_usefull_fcts as usfll

rho_list = np.random.randn(50)*0.2+24                    #Chose some random values of rho close to 24
t = np.arange(0,100,0.1)                                        #Timespan over which the trajectory is computed

data = usfll.create_data(rho_list,t,dist=0.1)           #Initial conditions close to origin

fig,ax = plt.subplots(3,1,sharex=True,figsize=(5,8))                                      #plot results
fig.suptitle(r'Change of conv. for traj. starting close to the origin')
x = np.linspace(np.min(rho_list),np.max(rho_list),100)
ylabels = ['x','y','z']
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
