import numpy as np
import matplotlib.pyplot as plt
import copy
import random
import math
import Functions

# Variables
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

def SelectBest(population):

    best = population[0]

    for element in population:
        if (element.f < best.f):
            best = element

    return best

def CalculateMean(population):
    mean = 0

    for i in range(len(population)):
        mean = mean + population[i].f

    mean = mean / D

    return mean


# Differential Evolution algortihm
def TLBO(xDimension, yDimension, step, funcName):

    for exp in range(num_experiments):
        count = 0
        # Generate population
        pop = GeneratePopulation(funcName, xDimension, yDimension)

        popmean = CalculateMean(pop)

        best = SelectBest(pop)

        while count < max_ofe:
            # Teacher phase
            r = np.random.uniform()
            Tf = np.random.randint(1,3)
            diff = r * (best.f - Tf * popmean)

            newTeacher = copy.deepcopy(best)

            for j in range(D):
                newTeacher.position[j] = newTeacher.position[j] + diff

                if (newTeacher.position[j] < xDimension): newTeacher.position[j] = xDimension
                if (newTeacher.position[j] > yDimension): newTeacher.position[j] = yDimension
            
            # Eval new teacher
            newTeacher.f = Functions.getFunctionZ(funcName, D, newTeacher.position)

            # Change teacher if better
            if (newTeacher.f < best.f):
                best.position = newTeacher.position
                best.f = newTeacher.f


            #Student phase
            for xi in pop:
                if (xi.id == best.id):
                    continue
                
                xj = random.choice(pop)
                while (xj.id == xi.id): #select randomly again to ensure we get another student
                    xj = random.choice(pop)

                newStudent = copy.deepcopy(xi)
                if (xi.f < xj.f):
                    for j in range(D):
                        newStudent.position[j] = xi.position[j] + r * (xi.position[j] - xj.position[j])
                        if (newStudent.position[j] < xDimension): newStudent.position[j] = xDimension
                        if (newStudent.position[j] > yDimension): newStudent.position[j] = yDimension
                else:
                    for j in range(D):
                        newStudent.position[j] = xi.position[j] + r * (xj.position[j] - xi.position[j])
                        if (newStudent.position[j] < xDimension): newStudent.position[j] = xDimension
                        if (newStudent.position[j] > yDimension): newStudent.position[j] = yDimension

                newStudent.f = Functions.getFunctionZ(funcName, D, newStudent.position)
                count = count + 1

                if (newStudent.f < xi.f):
                    xi.position = newStudent.position
                    xi.f = newStudent.f

        expBest = SelectBest(pop)
        print(expBest.f)

        
if __name__ == "__main__":
    print("Sphere Function")
    print("TLBO")
    # Sphere
    TLBO(-5.12, 5.12, 0.25, 'sphere')
    print("MEAN")
    print("")

    print("Schwefel Function")
    print("TLBO")
    #Schwefel function
    TLBO(-500, 500, 15, "schwefel")
    print("MEAN")
    print("")

    print("Griewank Function")
    print("TLBO")
    #Griewank
    TLBO(-600, 600, 10, "griewank")
    print("MEAN")
    print("")

    print("Rastrigin Function")
    print("TLBO")
    #Rastrigin
    TLBO(-5.12, 5.12, 0.25, "rastrigin")
    print("MEAN")
    print("")

    print("Lewy Function")
    print("TLBO")
    #Lewy
    TLBO(-10, 10, 0.25, "lewy")
    print("MEAN")
    print("")

    print("Michalewitz Function")
    print("TLBO")
    #Michalewitz
    TLBO(0, np.pi, 0.05, "michalewitz")
    print("MEAN")
    print("")

    print("Zakharov Function")
    print("TLBO")
    #Zakharov
    TLBO(-5, 10, 0.5, "zakharov")
    print("MEAN")
    print("")

    print("Ackley Function")
    print("TLBO")
    #Ackley -32.768 až 32.768
    TLBO(-5.768, 5.768, 0.1, "ackley")
    print("MEAN")
    print("")