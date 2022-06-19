import matplotlib.pyplot as plt
import numpy as np
import Homework5_usefull_fcts as usfll

rho_list = np.abs(np.random.randn(30)*1.5)                      #Chose some random positive values of rho
t = np.arange(0,100,0.1)                                        #Timespan over which the trajectory is computed

data = usfll.create_data(rho_list,t,dist=1)                     #Initial conditions close to the origin

norms_final = np.zeros(len(rho_list))                            #Calculate norms of the final and initial points
norms_init = np.zeros(len(rho_list))    
for i in range(len(rho_list)):
    norms_final[i] = np.linalg.norm(data[i,4:])
    norms_init[i] = np.linalg.norm(data[i,1:3])

plt.scatter(data[:,0],norms_final,color='black',s=30,label='final point')                       #Plot results
plt.scatter(data[:,0],norms_init,color='gray',s=8,label='initial point')  
plt.grid()
plt.title('Conv. of traj. starting close to 0')
plt.xlabel(r'$\rho$')
plt.ylabel(r'$\lim_{t \to \infty} \; ||\vec{x}||$')
plt.legend()
plt.show()

