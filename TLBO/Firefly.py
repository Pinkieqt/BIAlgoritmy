import numpy as np
import matplotlib.pyplot as plt
import copy
import random
import math
import Functions

# Control parameters
pop_size = 30
M_max = 3000 # MaxGeneration
B0 = 1
alfa = 0.3
D = 30
num_experiments = 30

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
        for j in range(D):
            position.append(np.random.uniform(xDimension, yDimension))
        
        brght = Functions.getFunctionZ(funcName, D, position)
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

    for exp in range(num_experiments):

        # Generate new population of size pop_size
        population = GeneratePopulation(funcName, xDimension, yDimension)

        m = 0

        # Get best member from current population
        bestMember = population[0]
        bestMember = FindBestMember(bestMember, population)

        while m < M_max:

            for i in population:
                if i.id == bestMember.id:
                    # Move best member randomly
                    MoveBest(bestMember, (xDimension, yDimension, step))
                    # Evaulate
                    bestMember.brightness = Functions.getFunctionZ(funcName, D, bestMember.position)
                    m = m + 1
                    continue

                for j in population:
                    if j.brightness < i.brightness:
                        # Move firefly
                        MoveFirefly(i, j, (xDimension, yDimension, step))

                        # Evaulate brigthness
                        i.brightness = Functions.getFunctionZ(funcName, D, i.position)
                        m = m + 1


            # Find best again
            bestMember = FindBestMember(bestMember, population)

        print(bestMember.brightness)
        
if __name__ == "__main__":
    print("Sphere Function")
    print("FireflyAlg")
    # Sphere
    FireflyAlg(-5.12, 5.12, 0.25, 'sphere')
    print("MEAN")
    print("")

    print("Schwefel Function")
    print("FireflyAlg")
    #Schwefel function
    FireflyAlg(-500, 500, 15, "schwefel")
    print("MEAN")
    print("")

    print("Griewank Function")
    print("FireflyAlg")
    #Griewank
    FireflyAlg(-600, 600, 10, "griewank")
    print("MEAN")
    print("")

    print("Rastrigin Function")
    print("FireflyAlg")
    #Rastrigin
    FireflyAlg(-5.12, 5.12, 0.25, "rastrigin")
    print("MEAN")
    print("")

    print("Lewy Function")
    print("FireflyAlg")
    #Lewy
    FireflyAlg(-10, 10, 0.25, "lewy")
    print("MEAN")
    print("")

    print("Michalewitz Function")
    print("FireflyAlg")
    #Michalewitz
    FireflyAlg(0, np.pi, 0.05, "michalewitz")
    print("MEAN")
    print("")

    print("Zakharov Function")
    print("FireflyAlg")
    #Zakharov
    FireflyAlg(-5, 10, 0.5, "zakharov")
    print("MEAN")
    print("")

    print("Ackley Function")
    print("FireflyAlg")
    #Ackley -32.768 až 32.768
    FireflyAlg(-5.768, 5.768, 0.1, "ackley")
    print("MEAN")
    print("")