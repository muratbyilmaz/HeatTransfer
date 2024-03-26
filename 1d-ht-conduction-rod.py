import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

### 1D HEAT TRANSFER ON ROD
L = 25 # length of the rod
Lx = 150 # points along the length
Ts = 10 # Simulation time
nt = 200 # number of time steps

x = np.linspace(0,L,Lx)
k = 0.2
h = L/(Lx-1)

dudt = []
def diff_func(u,t):
    dudt = np.ones(x.shape)
    dudt[0] = 0
    dudt[-1] = 0

    for i in range(1,Lx-1):
        dudt[i] = k*(u[i+1] - 2*u[i] + u[i-1])/h**2
    return dudt

Tmax = 150
in_temp = Tmax*np.ones(x.shape)*np.sin(np.pi*x/L)

tspan = np.linspace(0.0,Ts,nt)
solve = odeint(diff_func, in_temp, tspan)

for i in range(len(tspan)):
    plt.clf()
    plt.plot(x,solve[0],label="initial Temperature")
    plt.plot(x,solve[i],label="Current Temperature")
    heading = "Time $t$ = " + str(tspan[i]) + "s, $T_{max}$ =" + str(np.amax(solve[i])) + "$^o C$"
    plt.suptitle(heading)
    plt.title("Heat Diffusion in Rod - 1D")
    plt.xlim(0,L)
    plt.ylim(0, Tmax+15)
    plt.grid()
    plt.xlabel('X')
    plt.ylabel('T(X)')
    plt.legend()
    plt.pause(0.01)


#https://en.wikipedia.org/wiki/Finite_difference_method
