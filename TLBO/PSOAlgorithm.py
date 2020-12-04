import numpy as np
import matplotlib.pyplot as plt
import copy
import random
import math
import Functions

# Control parameters
pop_size = 30 #number of individuals
M_max = 3000 #number of migration cycles
c1 = 2.0 #learning constant 1
c2 = 2.0 #learning constant 2
vmin = -1 #min velocity
vmax = 1 #max velocity
D = 30 #dimension
num_experiments = 30

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
        velocity = []
        for i in range(D):
            position.append(np.random.uniform(xDimension, yDimension))
            velocity.append(np.random.uniform(vmin, vmax))
        position.append(Functions.getFunctionZ(funcName, D, position))
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
    tmp.position[D] = Functions.getFunctionZ(funcName, D, tmp.position)

    # Compare to its pBest
    if (tmp.position[D] <= tmp.pBestPos[D]):
        tmp.pBestPos = copy.deepcopy(tmp.position)
    
    return tmp

def SelectBest(population):

    best = population[0]

    for element in population:
        if (element.position[D] < best.position[D]):
            best = element

    return best

# Particle Swarm Optimalization algorithm
def ParticleSwarm(xDimension, yDimension, step, funcName):

    for exp in range(num_experiments):

        # Generate pop_size random individuals
        population = GenerateSwarm(funcName, xDimension, yDimension)

        # Select initial best
        gBest = population[0]
        m = 0

        while m < M_max:
            for particle in population:
                # Calculate velocity
                particle = CalculateParticleVelocity(particle, gBest)
                
                # Calculate new position
                particle = CalculateParticlePosition(particle, xDimension, yDimension, funcName, step)
                m = m + 1

                if (particle.pBestPos[D] <= gBest.pBestPos[D]):
                    gBest.pBestPos = copy.deepcopy(particle.pBestPos)


        expBest = SelectBest(population)
        print(expBest.position[D])

if __name__ == "__main__":
    print("Sphere Function")
    print("ParticleSwarm")
    # Sphere
    ParticleSwarm(-5.12, 5.12, 0.25, 'sphere')
    print("MEAN")
    print("")

    print("Schwefel Function")
    print("ParticleSwarm")
    #Schwefel function
    ParticleSwarm(-500, 500, 15, "schwefel")
    print("MEAN")
    print("")

    print("Griewank Function")
    print("ParticleSwarm")
    #Griewank
    ParticleSwarm(-600, 600, 10, "griewank")
    print("MEAN")
    print("")

    print("Rastrigin Function")
    print("ParticleSwarm")
    #Rastrigin
    ParticleSwarm(-5.12, 5.12, 0.25, "rastrigin")
    print("MEAN")
    print("")

    print("Lewy Function")
    print("ParticleSwarm")
    #Lewy
    ParticleSwarm(-10, 10, 0.25, "lewy")
    print("MEAN")
    print("")

    print("Michalewitz Function")
    print("ParticleSwarm")
    #Michalewitz
    ParticleSwarm(0, np.pi, 0.05, "michalewitz")
    print("MEAN")
    print("")

    print("Zakharov Function")
    print("ParticleSwarm")
    #Zakharov
    ParticleSwarm(-5, 10, 0.5, "zakharov")
    print("MEAN")
    print("")

    print("Ackley Function")
    print("ParticleSwarm")
    #Ackley -32.768 až 32.768
    ParticleSwarm(-5.768, 5.768, 0.1, "ackley")
    print("MEAN")
    print("")