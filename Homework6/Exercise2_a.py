from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0,100,0.001)
u0 = [1,1,1]

#Define Lorenz System
sigma = 10
beta = 8/3
rho = 28

def lorenz(x,t,rho):   
    return [-sigma*(x[0]-x[1]), rho*x[0]-x[1]-x[0]*x[2], x[0]*x[1]-beta*x[2]]

tr = odeint(lorenz,u0,t,args=(rho,))

fig = plt.figure()                                      #Plot Trajectory
ax = plt.axes(projection='3d')
ax.plot3D(tr[:,0],tr[:,1],tr[:,2])
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()


    