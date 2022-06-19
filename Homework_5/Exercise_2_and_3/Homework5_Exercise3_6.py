import matplotlib.pyplot as plt
import numpy as np
import Homework5_usefull_fcts as usfll

delta_rho = 1                                                   #Determine how much the observed value of rho should differ from rho_H
rho = usfll.rho_H-delta_rho
rho_list = np.ones(100)*(rho)          
C_plus = usfll.C_plus_minus(rho)[0]        
t = np.arange(0,100,0.1)                                        #Timespan over which the trajectory is computed

init_pnts = np.zeros((len(rho_list),3))                         #Set initial conditions to C_+
for i in range(len(init_pnts)):
    init_pnts[i,:] = usfll.C_plus_minus(rho_list[i])[0]

def find_conv_pnts(data):                                       #Find the converging and diverging points for given data
    conv_pnts = []                                                  
    div_pnts = []
    for i in data:
        final = i[4:]
        if np.linalg.norm(final-C_plus) < 1:
            conv_pnts.append(i)
        else:
            div_pnts.append(i)
    conv_pnts = np.array(conv_pnts)
    div_pnts = np.array(div_pnts)
    return [conv_pnts,div_pnts]

fig,ax = plt.subplots(3,1,figsize=(5,8))             #plot results
fig.suptitle(f'Conv. of traj. depending on initial conds. for $\\rho = \\rho_H -${delta_rho}')
x = np.linspace(np.min(rho_list),np.max(rho_list),100)
labels = ['x','y','z']
for i,curr_ax in enumerate(ax):
    data = usfll.create_data(rho_list,t,dist=10,init_pnt=init_pnts,no_rand=[(i+2)%3])        #Create data where the coord which is not considered has no randomness
    conv_pnts,div_pnts = find_conv_pnts(data)
    curr_ax.scatter(div_pnts[:,1+i%3],div_pnts[:,1+(i+1)%3],color='black',s=8,label='divergent')
    curr_ax.scatter(conv_pnts[:,1+i%3],conv_pnts[:,1+(i+1)%3],color='red',s=8,label='convergent')
    curr_ax.scatter(C_plus[i%3],C_plus[(i+1)%3],color='blue',s=80,label=r'$C_+$',marker='x')
    curr_ax.grid()
    curr_ax.set_xlabel(labels[i%3])
    curr_ax.set_ylabel(labels[(i+1)%3])

ax[2].legend()
plt.tight_layout()
plt.show()
