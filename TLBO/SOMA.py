import numpy as np
import matplotlib.pyplot as plt
import copy
import random
import math
import Functions

# Control parameters
pop_size = 30 
PRT = 0.4
PathLength = 3.0
Step = 0.11
M_max = 3000
D = 30
num_experiments = 30

# Particle class
class Member:
    def __init__(self, individual_id, position, f):
        self.id = individual_id
        # Position x, y, z
        self.position = position
        self.f = f

# Function to generate swarm
def GeneratePopulation(funcName, xDimension, yDimension):
    population = []
    for i in range(pop_size):
        position = []
        for j in range(D):
            position.append(np.random.uniform(xDimension, yDimension))
        
        f = Functions.getFunctionZ(funcName, D, position)
        population.append(Member(i, position, f))
    
    return population

# Find best member in population
def FindBestMember(currentPopulation):
    bestMember = currentPopulation[0]
    for member in currentPopulation:
        if(member.f < bestMember.f):
            bestMember = member
    
    return bestMember

# Particle Swarm Optimalization algorithm
def SOMA(xDimension, yDimension, step, funcName):

    for exp in range(num_experiments):


        # Generate new population of size pop_size
        population = GeneratePopulation(funcName, xDimension, yDimension)

        m = 0

        while m < M_max:

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
                    f = Functions.getFunctionZ(funcName, D, tmpPos)
                    m = m + 1

                    # Check if F of temporary member is better than F of current member
                    if f < newBest.f:
                        newBest.position = tmpPos
                        newBest.f = f
                    
                    # Increment t
                    t = t + Step

                # Add new member to current population
                newPopulation.append(newBest)

            # Replace old population with the new one
            population = copy.deepcopy(newPopulation)

        
        # select best
        expBest = FindBestMember(population)
        print(expBest.f)

if __name__ == "__main__":
    print("Sphere Function")
    print("SOMA")
    # Sphere
    SOMA(-5.12, 5.12, 0.25, 'sphere')
    print("MEAN")
    print("")

    print("Schwefel Function")
    print("SOMA")
    #Schwefel function
    SOMA(-500, 500, 15, "schwefel")
    print("MEAN")
    print("")

    print("Griewank Function")
    print("SOMA")
    #Griewank
    SOMA(-600, 600, 10, "griewank")
    print("MEAN")
    print("")

    print("Rastrigin Function")
    print("SOMA")
    #Rastrigin
    SOMA(-5.12, 5.12, 0.25, "rastrigin")
    print("MEAN")
    print("")

    print("Lewy Function")
    print("SOMA")
    #Lewy
    SOMA(-10, 10, 0.25, "lewy")
    print("MEAN")
    print("")

    print("Michalewitz Function")
    print("SOMA")
    #Michalewitz
    SOMA(0, np.pi, 0.05, "michalewitz")
    print("MEAN")
    print("")

    print("Zakharov Function")
    print("SOMA")
    #Zakharov
    SOMA(-5, 10, 0.5, "zakharov")
    print("MEAN")
    print("")

    print("Ackley Function")
    print("SOMA")
    #Ackley -32.768 až 32.768
    SOMA(-5.768, 5.768, 0.1, "ackley")
    print("MEAN")
    print("")