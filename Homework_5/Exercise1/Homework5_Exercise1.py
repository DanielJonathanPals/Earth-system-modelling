from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np

plt.close('all')
t = np.arange(0,100,0.1)

def f(x,t,alpha,gamma,g,rho_p):                 #RHS of ODE
    z = x[0]
    v = x[1]
    z_dot_dot = g*(alpha*z+gamma*z**3)/rho_p
    return [v,z_dot_dot]

alpha_values=[-1,0,1,2]                         #Diffent values for alpha
fig,ax = plt.subplots(2,2)
for j,alpha in enumerate(alpha_values):
    for i in range(10):
        u0 = np.random.randn(2)*0.5             #Random initial conditions
        tr = odeint(f,u0,t,args=(alpha,-1,10,10))   #solve ODE
        curr_ax = ax.flat[j]
        curr_ax.plot(tr[:,0],tr[:,1],color='black')
        curr_ax.set_title(f'$\\alpha$ = {alpha}')
        curr_ax.set_xlabel('z')
        curr_ax.set_ylabel('v')
fig.suptitle('Solutions of the system')
plt.tight_layout()
plt.show()
