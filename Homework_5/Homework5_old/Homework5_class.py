from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d


class DynamicalSystems:
    """
    class that can be used to analyse a given dynamical system.
    """
    def __init__(self, f):
        """
        Initialise an istant of DynamicalSystems

        Arguments:
        - f: (function), is the function describing the RHS of the dynamical system.
            It has to be of the form f(x,t,p1,p2,...), where x is the vector in phase
            space, t is the time argument and p1,p2,... are additional parameters.
        """
        self.f = f

    def trajectory(self,u0,t,prms):
        """
        Calculates the trajectory of the System for given initial conditions and time span.

        Arguments:
        - u0: (np.array), Initial conditions
        - t: (np.array), time span over which to solve
        - prms: (tuple), tuple parameters to use in f

        Returns:
        - np.array of dimension (length(t),length(u0)) with the trajectory at the given times
        """
        tr = odeint(self.f,u0,t,args=prms)
        return tr

    def plot_phase_space(self,xlims,ylims,dx,dy,scale=1):
        """
        Plots the phase space of the system with vectors starting at grid points with spacing
        dx, dy.

        Arguments:
        - xlims: ()
        """

