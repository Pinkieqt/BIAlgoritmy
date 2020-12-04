import numpy as np
import matplotlib.pyplot as plt
import copy
import random
import math
import Functions

# Control parameters
pop_size = 20 
M_max = 20 # MaxGeneration
B0 = 1
alfa = 0.3
D = 2

# Particle class
class Firefly:
    def __init__(self, individual_id, position, brght):
        self.id = individual_id
        # Position x, y, z
        self.position = position
        self.brightness = brght
        

# Function to generate swarm
def GeneratePopulation(funcName, xDimension, yDimension):
    population = []
    for i in range(pop_size):
        position = []
        position.append(np.random.uniform(xDimension, yDimension))
        position.append(np.random.uniform(xDimension, yDimension))
        brght = Functions.getFunctionZ(funcName, position[0], position[1])
        population.append(Firefly(i, position, brght))
    
    return population

# Find best member in population
def FindBestMember(best, currentPopulation):
    bestMember = best
    for member in currentPopulation:
        if(member.brightness < bestMember.brightness):
            bestMember = member
    
    return bestMember

# Move best
def MoveBest(best, dim):
    for i in range(D): 
        # dim[2] = step of function -> make movement bigger or smaller according to used function
        best.position[i] = best.position[i] + (alfa * np.random.normal(0, 1)) * dim[2]

        # Check dimensions
        if (best.position[i] < dim[0]): best.position[i] = dim[0]
        if (best.position[i] > dim[1]): best.position[i] = dim[1]

# Move other firefly than best > moving I towards J
def MoveFirefly(i, j, dim):
    #dist = np.linalg.norm(np.array(i.position) - np.array(j.position))
    dist = math.sqrt((i.position[0] - j.position[0])**2 + (i.position[1] - j.position[1])**2 + (i.brightness - j.brightness)**2)

    for x in range(D):
        i.position[x] = i.position[x] + ((B0 / (1 + dist)) * (j.position[x] - i.position[x]) + alfa * np.random.normal(0, 1)) * dim[2]

        # Check dimensions
        if (i.position[x] < dim[0]): i.position[x] = dim[0]
        if (i.position[x] > dim[1]): i.position[x] = dim[1]
    

# Firefly optimization
def FireflyAlg(xDimension, yDimension, step, funcName):
    # Graph
    plt.ion()
    fig = plt.figure()
    fig.suptitle("Firefly")
    ax = fig.add_subplot(111, projection='3d')

    # Function plot
    x = y = np.arange(xDimension, yDimension, step)
    X, Y = np.meshgrid(x, y)
    Z = np.array([Functions.getFunctionZ(funcName, x, y) for x,y in zip(np.ravel(X), np.ravel(Y))]) 
    Z = Z.reshape(X.shape)


    # Generate new population of size pop_size
    population = GeneratePopulation(funcName, xDimension, yDimension)

    m = 0

    # Get best member from current population
    bestMember = population[0]
    bestMember = FindBestMember(bestMember, population)

    print("Interrupt program from terminal to stop before finishing.")
    while m < M_max:
        print("Migration: " + str(m))

        for i in population:
            if i.id == bestMember.id:
                # Move best member randomly
                MoveBest(bestMember, (xDimension, yDimension, step))
                # Evaulate
                bestMember.brightness = Functions.getFunctionZ(funcName, bestMember.position[0], bestMember.position[1])
                continue

            for j in population:
                if j.brightness < i.brightness:
                    # Move firefly
                    MoveFirefly(i, j, (xDimension, yDimension, step))

                    # Evaulate brigthness
                    i.brightness = Functions.getFunctionZ(funcName, i.position[0], i.position[1])


        # Find best again
        bestMember = FindBestMember(bestMember, population)


        # Graph
        plt.cla()
        for element in population:
            ax.scatter(element.position[0], element.position[1], element.brightness, color="black", s=10)
        ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='cool', alpha=0.35)
        plt.pause(0.0000001)
        plt.draw()

        # Increment loop condition
        m = m + 1

    #After loop show graph
    print("Done!")
    print("Press any key to close graph.")
    plt.waitforbuttonpress()

        
if __name__ == "__main__":
    #Sphere
    FireflyAlg(-5.12, 5.12, 0.25, 'sphere')

    #Schwefel function
    #FireflyAlg(-500, 500, 15, "schwefel")

    #Griewank
    #FireflyAlg(-600, 600, 10, "griewank")

    #Rastrigin
    #FireflyAlg(-5.12, 5.12, 0.25, "rastrigin")

    #Lewy
    #FireflyAlg(-10, 10, 0.25, "lewy")

    #Michalewitz
    #FireflyAlg(0, np.pi, 0.05, "michalewitz")

    #Zakharov
    #FireflyAlg(-5, 10, 0.5, "zakharov")

    #Ackley -32.768 až 32.768
    #FireflyAlg(-5.768, 5.768, 0.1, "ackley")