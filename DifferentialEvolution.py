import numpy as np
import matplotlib.pyplot as plt
import copy
import random
import math
import Functions

# Variables
NP = 20
CR = 0.5
Gmax = 50
F = 0.5
dimension = 2

# Individual class
class IndividualPoint:
    def __init__(self, individual_id, x, y, z):
        self.id = individual_id
        self.x = x
        self.y = y
        self.z = z

# Function to generate population
def GeneratePopulation(funcName, xDimension, yDimension):
    population = []
    for i in range(NP):
        x = np.random.uniform(xDimension, yDimension)
        y = np.random.uniform(xDimension, yDimension)
        z = Functions.getFunctionZ(funcName, x, y)
        population.append(IndividualPoint(i, x, y, z))
    
    return population

# Function to compute mutation vector
def ComputeMutationVector(r1, r2, r3, xDim, yDim):
    x = (r1.x - r2.x)*F + r3.x
    y = (r1.y - r2.y)*F + r3.y
    z = (r1.z - r2.z)*F + r3.z

    if (x < xDim): x = xDim
    if (y < xDim): y = xDim
    if (z < xDim): z = xDim

    if (x > yDim): x = yDim
    if (y > yDim): y = yDim
    if (z > yDim): z = yDim

    return IndividualPoint(99, x, y, z)

# Differential Evolution algortihm
def DifferentialEvolution(xDimension, yDimension, step, funcName):
    # Graph
    plt.ion()
    fig = plt.figure()
    fig.suptitle("Differential Evolution")
    ax = fig.add_subplot(111, projection='3d')

    # Function plot
    x = y = np.arange(xDimension, yDimension, step)
    X, Y = np.meshgrid(x, y)
    Z = np.array([Functions.getFunctionZ(funcName, x, y) for x,y in zip(np.ravel(X), np.ravel(Y))]) 
    Z = Z.reshape(X.shape)

    # Generate population
    pop = GeneratePopulation(funcName, xDimension, yDimension)
    g = 0

    print("Interrupt program from terminal to stop before finishing.")
    while g < Gmax:
        print("Iteration n.: " + str(g))
        new_pop = copy.deepcopy(pop)
        
        for element in new_pop:
            # Get random indices
            r1, r2, r3 = random.sample(new_pop, k=3)
            while element.id == r1.id or element.id == r2.id or element.id == r3.id:
                r1, r2, r3 = random.sample(new_pop, k=3)
            
            # Mutation vector
            v = ComputeMutationVector(r1, r2, r3, xDimension, yDimension)

            # Trial vector
            u = np.zeros(dimension)
            j_rnd = np.random.randint(0, dimension)

            for j in range(dimension):
                if np.random.uniform() < CR or j == j_rnd:
                    if j == 0: u[j] = v.x 
                    else: u[j] = v.y
                else:
                    if j == 0: u[j] = element.x 
                    else: u[j] = element.y
            
            f_u = Functions.getFunctionZ(funcName, u[0], u[1])
            
            # Accept better or same solution
            if f_u <= element.z:
                new_x = IndividualPoint(element.id, u[0], u[1], f_u)
                pop[element.id] = new_x

        # Graph
        plt.cla()
        for element in new_pop:
            if (element.y > yDimension): print("y")
            ax.scatter(element.x, element.y, element.z, color="black", s=10)
            print(element.z)
        ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='cool', alpha=0.35)
        plt.pause(0.0000001)
        plt.draw()

        g += 1
    
    #After loop show graph
    print("Done!")
    print("Press any keyboard to close graph.")
    plt.waitforbuttonpress()
        
if __name__ == "__main__":
    # Sphere
    DifferentialEvolution(-5.12, 5.12, 0.25, 'sphere')

    #Schwefel function
    #DifferentialEvolution(-500, 500, 15, "schwefel")

    #Griewank
    #DifferentialEvolution(-600, 600, 10, "griewank")

    #Rastrigin
    #DifferentialEvolution(-5.12, 5.12, 0.25, "rastrigin")

    #Lewy
    #DifferentialEvolution(-10, 10, 0.25, "lewy")

    #Michalewitz
    #DifferentialEvolution(0, np.pi, 0.05, "michalewitz")

    #Zakharov
    #DifferentialEvolution(-5, 10, 0.5, "zakharov")

    #Ackley -32.768 až 32.768
    #DifferentialEvolution(-5.768, 5.768, 0.1, "ackley")