import numpy as np
import matplotlib.pyplot as plt
import copy
import random
import math
import Functions

# Variables
CR = 0.5
F = 0.5
D = 30
NP = 30 #population size
num_experiments = 30
max_ofe = 3000

# Individual class
class IndividualPoint:
    def __init__(self, individual_id, position, f):
        self.id = individual_id
        self.position = position
        self.f = f

# Function to generate population
def GeneratePopulation(funcName, xDimension, yDimension):
    population = []
    for i in range(NP):
        position = []
        for j in range(D):
            position.append(np.random.uniform(xDimension, yDimension))
        
        f = Functions.getFunctionZ(funcName, D, position)
        population.append(IndividualPoint(i, position, f))
    
    return population

# Function to compute mutation vector
def ComputeMutationVector(r1, r2, r3, xDim, yDim):

    newPositions = []

    for i in range(D):
        tmp = (r1.position[i] - r2.position[i]) * F + r3.position[i]
        
        if(tmp < xDim): tmp = xDim
        if(tmp > yDim): tmp = yDim

        newPositions.append(tmp)
    
    f = (r1.f - r2.f) * F + r3.f


    return IndividualPoint(99, newPositions, f)


def SelectBest(population):

    best = population[0]

    for element in population:
        if (element.f < best.f):
            best = element

    return best

# Differential Evolution algortihm
def DifferentialEvolution(xDimension, yDimension, step, funcName):

    for experiment in range(num_experiments):

        # Generate population
        pop = GeneratePopulation(funcName, xDimension, yDimension)
        OFECount = 0

        while OFECount < max_ofe:
            new_pop = copy.deepcopy(pop)
            
            for element in new_pop:
                # Get random indices
                r1, r2, r3 = random.sample(new_pop, k=3)
                while element.id == r1.id or element.id == r2.id or element.id == r3.id:
                    r1, r2, r3 = random.sample(new_pop, k=3)
                
                # Mutation vector
                v = ComputeMutationVector(r1, r2, r3, xDimension, yDimension)
                # Trial vector
                u = np.zeros(D)
                j_rnd = np.random.randint(0, D)

                for j in range(D):
                    if np.random.uniform() < CR or j == j_rnd:
                        u[j] = v.position[j]
                    else:
                        u[j] = element.position[j]
                
                f_u = Functions.getFunctionZ(funcName, D, u)
                OFECount = OFECount + 1
                
                # Accept better or same solution
                if f_u <= element.f:
                    new_x = IndividualPoint(element.id, u, f_u)
                    pop[element.id] = new_x
    
        finalBest = SelectBest(pop)
        print(str(finalBest.f))
        
if __name__ == "__main__":
    print("Sphere Function")
    print("DifferentialEvolution")
    # Sphere
    DifferentialEvolution(-5.12, 5.12, 0.25, 'sphere')
    print("MEAN")
    print("")

    print("Schwefel Function")
    print("DifferentialEvolution")
    #Schwefel function
    DifferentialEvolution(-500, 500, 15, "schwefel")
    print("MEAN")
    print("")

    print("Griewank Function")
    print("DifferentialEvolution")
    #Griewank
    DifferentialEvolution(-600, 600, 10, "griewank")
    print("MEAN")
    print("")

    print("Rastrigin Function")
    print("DifferentialEvolution")
    #Rastrigin
    DifferentialEvolution(-5.12, 5.12, 0.25, "rastrigin")
    print("MEAN")
    print("")

    print("Lewy Function")
    print("DifferentialEvolution")
    #Lewy
    DifferentialEvolution(-10, 10, 0.25, "lewy")
    print("MEAN")
    print("")

    print("Michalewitz Function")
    print("DifferentialEvolution")
    #Michalewitz
    DifferentialEvolution(0, np.pi, 0.05, "michalewitz")
    print("MEAN")
    print("")

    print("Zakharov Function")
    print("DifferentialEvolution")
    #Zakharov
    DifferentialEvolution(-5, 10, 0.5, "zakharov")
    print("MEAN")
    print("")

    print("Ackley Function")
    print("DifferentialEvolution")
    #Ackley -32.768 až 32.768
    DifferentialEvolution(-5.768, 5.768, 0.1, "ackley")
    print("MEAN")
    print("")