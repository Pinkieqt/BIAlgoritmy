import numpy as np
import matplotlib.pyplot as plt
import copy
import random
import math
import Functions

# Control parameters
pop_size = 20 #number of individuals
M_max = 50 #number of migration cycles
c1 = 2.0 #learning constant 1
c2 = 2.0 #learning constant 2
vmin = -1 #min velocity
vmax = 1 #max velocity
D = 2 #dimension


# Particle class
class Particle:
    def __init__(self, individual_id, position, velocity):
        self.id = individual_id
        # Position x, y, z
        self.position = position

        # Velocity x, y
        self.velocity = velocity

        # pBest x, y, z
        self.pBestPos = copy.deepcopy(position)

# Function to generate swarm
def GenerateSwarm(funcName, xDimension, yDimension):
    population = []
    for i in range(pop_size):
        position = []
        position.append(np.random.uniform(xDimension, yDimension))
        position.append(np.random.uniform(xDimension, yDimension))
        position.append(Functions.getFunctionZ(funcName, position[0], position[1]))
        velocity = []
        for i in range(D):
            velocity.append(np.random.uniform(vmin, vmax))
        population.append(Particle(i, position, velocity))
    
    return population

# Calculate velocity of Particle
def CalculateParticleVelocity(particle, gbest):
    tmp = particle

    for i in range(D):
        tmp.velocity[i] = particle.velocity[i] + c1 * np.random.uniform() * (particle.pBestPos[i] - particle.position[i]) + c2 * np.random.uniform() * (gbest.pBestPos[i] - particle.position[i])
        
        # Check boundaries
        if(tmp.velocity[i] > vmax): tmp.velocity[i] = vmax
        if(tmp.velocity[i] < vmin): tmp.velocity[i] = vmin

    return tmp

# Calculate position of Particle
def CalculateParticlePosition(particle, xDim, yDim, funcName, step):
    tmp = particle

    # Calculate new position
    for i in range(D):
        tmp.position[i] = tmp.position[i] + step * tmp.velocity[i]

        # Check boundaries
        if (tmp.position[i] < xDim): tmp.position[i] = xDim
        if (tmp.position[i] > yDim): tmp.position[i] = yDim

    # Calculate Z
    tmp.position[D] = Functions.getFunctionZ(funcName, tmp.position[0], tmp.position[1])

    # Compare to its pBest
    if (tmp.position[D] < tmp.pBestPos[D]):
        tmp.pBestPos = copy.deepcopy(tmp.position)
    
    return tmp

# Find best member in population
def FindBestMember(best, currentPopulation):
    bestMember = best
    for member in currentPopulation:
        if(member.pBestPos[D] < bestMember.pBestPos[D]):
            bestMember = member
    
    return bestMember



# Particle Swarm Optimalization algorithm
def ParticleSwarm(xDimension, yDimension, step, funcName):
    # Graph
    plt.ion()
    fig = plt.figure()
    fig.suptitle("Particle Swarm Optimalization")
    ax = fig.add_subplot(111, projection='3d')

    # Function plot
    x = y = np.arange(xDimension, yDimension, step)
    X, Y = np.meshgrid(x, y)
    Z = np.array([Functions.getFunctionZ(funcName, x, y) for x,y in zip(np.ravel(X), np.ravel(Y))]) 
    Z = Z.reshape(X.shape)


    # Generate pop_size random individuals
    population = GenerateSwarm(funcName, xDimension, yDimension)

    # Select initial best
    gBest = population[0]
    gBest = FindBestMember(gBest, population)
    m = 0

    print("Interrupt program from terminal to stop before finishing.")
    while m < M_max:
        print("Iteration n.: " + str(m))
        for particle in population:
            # Calculate velocity
            particle = CalculateParticleVelocity(particle, gBest)
            
            # Calculate new position
            particle = CalculateParticlePosition(particle, xDimension, yDimension, funcName, step)

            if (particle.position[D] < gBest.pBestPos[D]):
                gBest.pBestPos = particle.position
                print(gBest.pBestPos[D])

        # Graph
        plt.cla()
        for element in population:
            ax.scatter(element.pBestPos[0], element.pBestPos[1], element.pBestPos[D], color="black", s=10)
        ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='cool', alpha=0.35)
        plt.pause(0.0000001)
        plt.draw()

        m = m + 1


    #After loop show graph
    print("Done!")
    print("Press any key to close graph.")
    plt.waitforbuttonpress()

        
if __name__ == "__main__":
    #Sphere
    #ParticleSwarm(-5.12, 5.12, 0.25, 'sphere')

    #Schwefel function
    #ParticleSwarm(-500, 500, 15, "schwefel")

    #Griewank
    #ParticleSwarm(-600, 600, 10, "griewank")

    #Rastrigin
    #ParticleSwarm(-5.12, 5.12, 0.25, "rastrigin")

    #Lewy
    #ParticleSwarm(-10, 10, 0.25, "lewy")

    #Michalewitz
    #ParticleSwarm(0, np.pi, 0.05, "michalewitz")

    #Zakharov
    ParticleSwarm(-5, 10, 0.5, "zakharov")

    #Ackley -32.768 až 32.768
    #ParticleSwarm(-5.768, 5.768, 0.1, "ackley")