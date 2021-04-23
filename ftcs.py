import numpy as np
import matplotlib.pyplot as plt
import time

def psi(x, L, C, sigma):
    return C*((x*(L-x))/L**2)*np.exp((-1*(x-d)**2)/(2*sigma**2))

def phi(x, L, C, sigma, h):
    return (C*((x*(L-x))/L**2)*np.exp((-1*(x-d)**2)/(2*sigma**2)))*h

if __name__ == '__main__':
    L = 1 #Length of string in meters
    d = 0.1 #meters where hammer strikes string
    C = 1 #m/s
    sigma = 0.3 #meters
    a = 0.01 #meters, grid spacing
    h = 1e-6 # timestep in seconds
    v = 100 #m/s

    xs = np.arange(0, L+a, a)
    ys = np.zeros(xs.shape)
    newYs = ys.copy()

    t = 0 #seconds
    tend = 1 #seconds

    iteration = 0
    times = []
    ylist = []
    timelist = []
    while t < tend:
        for i in range(len(ys)):
            iteration += 1
            times.append(t)
            ys[i] = psi(xs[i], L, C, sigma) + (v**2/a**2)*(phi(xs[i]+a, L, C, sigma, h)+
                                     phi(xs[i]-a, L, C, sigma, h)-
                                     2*phi(xs[i], L, C, sigma, h))
            t += h
        ylist.append(ys)
        timelist.append(times)
    print(iteration)
    print(newYs)
    plt.plot(xs, ys)
    plt.ylim(0, 1)
    plt.show()
##    plt.ion()
##    pl = plt.imshow(xs, ys)
##    for i in range(len(times)):
##        q = (xs, ylist[i])
##        pl.set_data(q)
##        plt.draw()
##        plt.pause(0.01)
        
        
        
