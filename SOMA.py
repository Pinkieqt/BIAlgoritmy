import numpy as np
import matplotlib.pyplot as plt
import copy
import random
import math
import Functions

# Control parameters
pop_size = 20 
PRT = 0.4
PathLength = 3.0
Step = 0.11
M_max = 100
D = 2

# Particle class
class Member:
    def __init__(self, individual_id, position):
        self.id = individual_id
        # Position x, y, z
        self.position = position

# Function to generate swarm
def GeneratePopulation(funcName, xDimension, yDimension):
    population = []
    for i in range(pop_size):
        position = []
        position.append(np.random.uniform(xDimension, yDimension))
        position.append(np.random.uniform(xDimension, yDimension))
        position.append(Functions.getFunctionZ(funcName, position[0], position[1]))
        population.append(Member(i, position))
    
    return population

# Find best member in population
def FindBestMember(currentPopulation):
    bestMember = currentPopulation[0]
    for member in currentPopulation:
        if(member.position[2] < bestMember.position[2]):
            bestMember = member
    
    return bestMember

# Particle Swarm Optimalization algorithm
def SOMA(xDimension, yDimension, step, funcName):
    # Graph
    plt.ion()
    fig = plt.figure()
    fig.suptitle("SOMA")
    ax = fig.add_subplot(111, projection='3d')

    # Function plot
    x = y = np.arange(xDimension, yDimension, step)
    X, Y = np.meshgrid(x, y)
    Z = np.array([Functions.getFunctionZ(funcName, x, y) for x,y in zip(np.ravel(X), np.ravel(Y))]) 
    Z = Z.reshape(X.shape)


    # Generate new population of size pop_size
    population = GeneratePopulation(funcName, xDimension, yDimension)

    m = 0

    print("Interrupt program from terminal to stop before finishing.")
    while m < M_max:
        print("Migration: " + str(m))

        newPopulation = []

        # Get best member from current population
        bestMember = FindBestMember(population)
        newPopulation.append(bestMember)

        for member in population:
            # Do not add bestMember as he is already inside of current new population
            if (bestMember.id == member.id):
                continue
            
            newBest = member
            t = Step
            
            while t < PathLength:
                # Generate PRTVector 
                PRTVector = []
                for d in range(D):
                    rnd = np.random.uniform()
                    PRTVector.append(1 if rnd < PRT else 0)

                tmpPos = []
                # Compute coordinates of new temporary member
                for d in range(D):
                    tmpPos.append(newBest.position[d] + (bestMember.position[d] - newBest.position[d]) * t * PRTVector[d])
                
                # Check boundaries of coordinates
                for d in range(D):
                    if (tmpPos[d] < xDimension): tmpPos[d] = xDimension
                    if (tmpPos[d] > yDimension): tmpPos[d] = yDimension

                # Compute F
                tmpPos.append(Functions.getFunctionZ(funcName, tmpPos[0],  tmpPos[1]))

                # Check if F of temporary member is better than F of current member
                if tmpPos[2] < newBest.position[2]:
                    #print("predtim:" + str(newBest.position[2]) + "____ted:" + str(tmpPos[2]))
                    newBest.position = tmpPos
                
                # Increment t
                t = t + Step

            # Add new member to current population
            newPopulation.append(newBest)


        # Graph
        plt.cla()
        for element in newPopulation:
            ax.scatter(element.position[0], element.position[1], element.position[2], color="black", s=10)
            print(element.position[2])
        ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='cool', alpha=0.35)
        plt.pause(0.0000001)
        plt.draw()

        # Replace old population with the new one
        population = copy.deepcopy(newPopulation)
        m = m + 1

    #After loop show graph
    print("Done!")
    print("Press any key to close graph.")
    plt.waitforbuttonpress()

        
if __name__ == "__main__":
    #Sphere
    SOMA(-5.12, 5.12, 0.25, 'sphere')

    #Schwefel function
    #SOMA(-500, 500, 15, "schwefel")

    #Griewank
    #SOMA(-600, 600, 10, "griewank")

    #Rastrigin
    #SOMA(-5.12, 5.12, 0.25, "rastrigin")

    #Lewy
    #SOMA(-10, 10, 0.25, "lewy")

    #Michalewitz
    #SOMA(0, np.pi, 0.05, "michalewitz")

    #Zakharov
    #SOMA(-5, 10, 0.5, "zakharov")

    #Ackley -32.768 až 32.768
    #SOMA(-5.768, 5.768, 0.1, "ackley")