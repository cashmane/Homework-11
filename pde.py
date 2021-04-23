import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    gridsize = 100 #nxn grid across box
    target = 1e-4 #target accuracy, in volts
    V = 1 #voltage at top of box
    a = 0.01
    epsilon_0 = 1

    #boundary condition
    phi = np.zeros((gridsize+1, gridsize+1))
    phi[20:41,60:81] = V
    phi[60:81,20:41] = -1*V
    print(phi)

    phiprime = np.zeros(phi.shape)

    max_diff = 1.0
    iteration = 0
    while max_diff > target:
        #calculate new values of potential
        for i in range(gridsize+1):
            for j in range(gridsize+1):
                if i == 0 or i == gridsize or j == 0 or j == gridsize:
                    phiprime[i,j] = phi[i,j]
                else:
                    phiprime[i,j] = 0.25*(phi[i+1, j]+
                                          phi[i-1, j]+
                                          phi[i, j+1]+
                                          phi[i, j-1])
        max_diff = np.max(abs(phi-phiprime))
        phi, phiprime = phiprime, phi

        #print(iteration, max_diff)
        iteration = iteration + 1
    print('The potential of the middle point is', phiprime[50,50])
    
    plt.imshow(phi)
    plt.legend()
    plt.title('Electric Potential')
    plt.show()
