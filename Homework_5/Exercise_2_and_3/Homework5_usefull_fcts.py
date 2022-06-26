from scipy.integrate import odeint
import numpy as np


sigma = 10
beta = 8/3
rho_H = sigma*(sigma+beta+3)/(sigma-beta-1)

def lorenz(x,t,rho):
    """
    Reruns RHS of the Lorenz System for sigma = 10, beta = 8/3 and given rho at point x

    Arguments:
    - x: (np.array) Array of size 3 describing the position where to evaluate the RHS
    - t: (FLoat64) only needed for odeint
    - rho: (Float64) Value of the parameter rho

    Returns:
    RHS of the Lorenz System
    """                 
    return [-sigma*(x[0]-x[1]), rho*x[0]-x[1]-x[0]*x[2], x[0]*x[1]-beta*x[2]]

def C_plus_minus(rho):                                       #
    """
    Calulate the position of C_+ and C_- for given value of rho.

    Arguments:
    - rho: (Float64) Value of rho
    """
    x = np.sqrt(beta*(rho-1))
    y = np.sqrt(beta*(rho-1))
    z = rho-1
    return [np.array([x,y,z]),np.array([-x,-y,z])]

def create_data(rho_list,t,dist=0.1,init_pnt=np.zeros(3),no_rand=[]):
    """
    Solves ODE for given timespan and diffentent given values of rho, where the 
    initial points are chosen randomly close to a given point.

    Arguments:
    - rho_list: (np.array) Array containing values of rho for which one wants solutions
    - t: (np.array) Array of dimension 1 ranging from 0 to the final time to which one wants to 
        compute the trajectory. This is given as an arguemt to the odeint solver
        of scipy
    - init_pnt: (np.array) Array of size 3 indicating the point close to witch the
        initial condition will randomly be chosen or Array of size (len(rho_list),3)
        with multiple initial points for the different values of rho.
    - dist: (Float64) Indicates how far from the init_pnt the random initial point 
        is chosen
    - no_rand: (list) is list that can consist of the values 0,1,2 and turns the randomess
        of the initial condition off for the respective coordinate x,y or z
    
    Returns:
    - Array of dimension len(rho_list)*nbr_of_sols,10 where the zeroth column holds
        the diffenent values of rho the first to third column hold the x,y and z coords.
        of the initial point and the fourth to sixt column hols the coordinates of the
        final point.
    """
    lns = len(rho_list)
    arr = np.zeros((lns,7))
    arr[:,0] = rho_list
    if np.shape(init_pnt) == (3,):                                              #Turn init_point into list of identical init points of only one is given 
        init_pnt = np.matmul(np.ones(lns).reshape(lns,1),init_pnt.reshape(1,3))
    for i in range(lns):
        u0 = np.random.randn(3)*dist+init_pnt[i]   
        for j in no_rand:
            u0[j]=init_pnt[i][j]      
        tr = odeint(lorenz,u0,t,args=(rho_list[i],))
        arr[i,1:] = np.concatenate((tr[0,:],tr[-1,:]))
    return arr