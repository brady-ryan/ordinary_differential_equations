import numpy as np
import matplotlib.pyplot as plt

G = 6.67e-11
Msun = 1.989e30
tmax = 365*24*60*60

class Orbit_ODE:

    def __init__(self,a,e,dt):

       self.a = a
       self.e = e
       self.dt = dt

    def initial_conditions(self):
        return np.array([0,self.a*(1-self.e),np.sqrt((G*Msun)/self.a * (1+self.e)/(1-self.e)),0])
    
    def rhs(self, vector):

     x, y, u, v = vector

     r = np.sqrt(x**2 + y**2)

     dxdt = u
     dydt = v

     dudt = (-G * Msun * x) / r**3
     dvdt = (-G * Msun * y) / r**3

     return np.array([dxdt,dydt,dudt,dvdt])
    
    def euler(self):

        history = []
        time = []
        dt = self.dt
        t = 0

        time.append(t)
        history.append(self.initial_conditions())

        while t < tmax:

            state_old = history[-1]

            if t + dt > tmax:
                dt = tmax - t

            dvec = self.rhs(state_old)

            state_new = state_old + dvec*dt

            t += dt

            time.append(t)
            history.append(state_new)

        return time, history
    
    def rk2(self):

        history = []
        time = []
        dt = self.dt
        t = 0

        time.append(t)
        history.append(self.initial_conditions())

        while t < tmax:

            if t + dt > tmax:
                dt = tmax - t

            state_old = history[-1]

            dvec = self.rhs(state_old)

            rk1 = state_old + 0.5*dt*dvec

            dvec = self.rhs(rk1)

            state_new = state_old + dt*dvec

            t += dt

            time.append(t)
            history.append(state_new)

        return time, history
    
    def plot(self):

            rtimes, rhistory = self.rk2()
            rxposition = [q[0] for q in rhistory]
            ryposition = [q[1] for q in rhistory]

            etimes, ehistory = self.euler()
            exposition = [q[0] for q in ehistory]
            eyposition = [q[1] for q in ehistory]

            fig, ax = plt.subplots(2)

            ax[0].plot(exposition,eyposition,'b-',label='Euler')
            ax[0].set_ylabel('Position (AU)')

            ax[1].plot(rxposition,ryposition,'g-',label='RK2')
            ax[1].set_ylabel('Position (AU)')
            ax[1].set_xlabel('Position (AU)')

            ax[0].set_title(rf'$\Delta$t = {self.dt}')
            plt.figlegend(loc = 'upper center', ncol=5, labelspacing=0.)

            plt.show()
    

dts = [1000,10000,100000,1000000]

for t in dts:
    earth = Orbit_ODE(1.496e11,0.06,t)

    earth.plot()
