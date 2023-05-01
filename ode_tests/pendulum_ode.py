import numpy as np
import matplotlib.pyplot as plt

g = 9.81

class Pendulum_ODE:

    def __init__(self,theta,w,L,dt):

        self.theta = theta
        self.w = w
        self.L = L
        self.dt = dt

    def initial_conditions(self):
        return np.array([self.theta,self.w])
    
    def rhs(self, vector):

        theta, w = vector

        domega = w

        dw = -g/self.L * np.sin(theta)

        return np.array([domega,dw])
    
    def euler(self):

        history = []
        time = []
        dt = self.dt
        tmax = 20
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
        tmax = 20
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
            ryposition = [q[0] for q in rhistory]

            etimes, ehistory = self.euler()
            eyposition = [q[0] for q in ehistory]

            fig, ax = plt.subplots(2)

            ax[0].plot(etimes,eyposition,'b-',label='Euler')
            ax[0].set_ylabel(r'$\theta$ (Radians)')

            ax[1].plot(rtimes,ryposition,'g-',label='RK2')
            ax[1].set_ylabel(r'$\theta$ (Radians)')
            ax[1].set_xlabel('Time (s)')

            ax[0].set_title(rf'$\Delta$t = {self.dt}')
            plt.figlegend(loc = 'upper center', ncol=5, labelspacing=0.)

            plt.show()
    

dts = [0.0001,0.001,0.01,0.1,.5]

for t in dts:
    vec = Pendulum_ODE(np.radians(100),0,10,t)

    vec.plot()
