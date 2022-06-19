import matplotlib.pyplot as plt
import numpy as np
import Homework5_usefull_fcts as usfll

rho_list = np.concatenate((np.abs(np.random.randn(50)*1.5),np.random.rand(100)*1.3*usfll.rho_H))  #Chose some random values of rho between 0 and 1.3*rho_H with espicially many points for small values
t = np.arange(0,100,0.1)                                        #Timespan over which the trajectory is computed

init_pnts = np.zeros((len(rho_list),3))                         #Randomly choose whether to start close to C_+ or C_-
for i in range(len(init_pnts)):
    if rho_list[i] <= 1:
        init_pnts[i,:] = np.zeros(3)
    else:
        init_pnts[i,:] = usfll.C_plus_minus(rho_list[i])[np.random.randint(0,2)]

data = usfll.create_data(rho_list,t,dist=1,init_pnt=init_pnts)                     #Initial conditions close to the origin

fig,ax = plt.subplots(3,1,sharex=True,figsize=(5,8))                                  #plot results
fig.suptitle(r'Bifurctaion diagram')
ylabels = ['x','y','z']
x = np.arange(1,usfll.rho_H,0.1)
for i,curr_ax in enumerate(ax):
    curr_ax.scatter(data[:,0],data[:,1+i],color='gray',s=8,label='initial point')
    curr_ax.scatter(data[:,0],data[:,4+i],color='black',s=30,label='final point')
    curr_ax.grid()
    curr_ax.set_xlabel(r'$\rho$')
    curr_ax.set_ylabel(ylabels[i])
    curr_ax.axvline(1,color='red',ls='--')
    curr_ax.axvline(usfll.rho_H,color='red',ls='--')

ax[2].legend()
plt.tight_layout()
plt.show()

