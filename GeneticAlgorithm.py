import numpy as np
import matplotlib.pyplot as plt
import copy
import random
import math

# City class
class City:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

# Individual class
class Individual:
    def __init__(self, name, route, routeLength):
        self.name = name
        self.route = route
        self.routeLength = routeLength

# Generate cities
def GenerateCities(Size, numOfCities):
    cities = []
    for i in range(numOfCities):
        rndX = random.randint(0, Size)
        rndY = random.randint(0, Size)
        cities.append(City(i, rndX, rndY))
    return cities

# Generate individual travelers
def GenerateIndividuals(NP, allCities):
    individuals = []
    #Generate NP individuals
    for i in range(NP):
        cities = copy.deepcopy(allCities)
        route = []
        #Start from first city
        initCity = cities.pop(0)
        firstCity = initCity
        route.append(initCity)
        routeLength = 0
        while cities:
            selection = cities.pop(random.randint(0, len(cities)-1))
            route.append(selection)
            lengthBetweenCities = math.sqrt((selection.x - initCity.x)**2 + (selection.y - initCity.y)**2) 
            routeLength = routeLength + lengthBetweenCities

            #Change city
            initCity = selection
        
        
        #Add route from latest city to the first one
        lengthBetweenCities = math.sqrt((firstCity.x - initCity.x)**2 + (firstCity.y - initCity.y)**2) 
        routeLength = routeLength + lengthBetweenCities

        individuals.append(Individual(i, route, routeLength))

    return individuals

# Crossover two individuals
def CrossoverIndividuals(A, B):
    middle_index = len(A.route)//2
    halfParent_A = A.route[:middle_index]

    for i in range(len(B.route)):
        isInside = False
        for j in range(len(halfParent_A)):
            if B.route[i].name == halfParent_A[j].name:
                isInside = True
        if isInside == False:
            halfParent_A.append(B.route[i])

    return halfParent_A

# Mutate individual
def MutateIndividual(individual):
    cities = copy.deepcopy(individual)
    rnd1 = random.randint(0, len(cities)-1)
    rnd2 = random.randint(0, len(cities)-1)

    tmp1 = cities[rnd1]
    cities[rnd1] = cities[rnd2]
    cities[rnd2] = tmp1

    return cities

# Evaulate individual
def EvaluateIndividual(individual):
    cities = copy.deepcopy(individual)
    firstCity = cities.pop(0)
    city = firstCity
    routeLength = 0

    while cities:
        selection = cities.pop(0)
        length = math.sqrt((selection.x - city.x)**2 + (selection.y - city.y)**2)
        routeLength = routeLength + length
        city = copy.deepcopy(selection)

    #Add route from latest city to the first one
    length = math.sqrt((firstCity.x - city.x)**2 + (firstCity.y - city.y)**2)
    routeLength = routeLength + length

    return routeLength

# Plot cities
def PlotCities(cities, ax):
    for i in range(len(cities)):
        if i == 0:
            ax.scatter(cities[i].x, cities[i].y, color="red", s=20)
            ax.annotate(str(i+1), (cities[i].x, cities[i].y), alpha=0.5)
        else:
            ax.scatter(cities[i].x, cities[i].y, color="black", s=10)
            ax.annotate(str(i+1), (cities[i].x, cities[i].y), alpha=0.5)

# Plot route across cities
def PlotRoute(route, routeLength):
    x = []
    y = []
    for i in range(len(route)):
        x.append(route[i].x)
        y.append(route[i].y)
    
    # get back to the starting city
    x.append(route[0].x)
    y.append(route[0].y)

    return x, y

# Genetic Algorithm
def GeneticAlg(NP, G, D, Size):
    #Graph
    plt.ion()
    fig = plt.figure()
    fig.suptitle("Genetický algoritmus")
    ax = fig.add_subplot()

    #Generate cities
    print("Generating cities")
    cities = GenerateCities(Size, D)

    #Generate first population and evaulate first population
    print("Generating population")
    population = GenerateIndividuals(NP, cities)

    #Lowest individual -> used to get the most lowest solution from all generations
    lowestIndividual = Individual(-1, [], Size*Size)

    print("Finding the best solution.......... ")
    for i in range(G):
        new_population = copy.deepcopy(population)

        for j in range(NP):
            parent_A = population[j]
            
            #Get parent_B .. parent_A != parent_B
            parent_B = population[random.randint(0, len(population)-1)]
            while parent_A.name == parent_B.name: #if random selected the same city then get another one
                parent_B = population[random.randint(0, len(population)-1)]
            
            #Crossover
            offspringAB = CrossoverIndividuals(parent_A, parent_B)

            #Mutate - 50% chance to mutate
            if np.random.uniform() < 0.5:
                offspringAB = MutateIndividual(offspringAB)

            #Evaulate offspring after crossover and mutation
            offspringLength = EvaluateIndividual(offspringAB)

            if (offspringLength < parent_A.routeLength):
                new_population[j] = Individual(population[j].name, offspringAB, offspringLength)

            if (offspringLength < lowestIndividual.routeLength):
                #print("Lower solution: " + str(offspringLength))
                lowestIndividual.route = offspringAB
                lowestIndividual.routeLength = offspringLength

                #Plot route
                plt.cla()
                PlotCities(cities, ax)
                x, y = PlotRoute(offspringAB, offspringAB)
                lengthText = "Vzdálenost trasy: " + str(round(lowestIndividual.routeLength, 2))
                plt.plot(x, y, color="red", alpha=0.5, linewidth=1)
                plt.xlabel(lengthText, color="red")
                plt.pause(0.0000001)
                plt.draw()

        population = new_population


    #After loop show graph
    print("Found!")
    print("Press any keyboard to close graph.")
    plt.show()   
    plt.waitforbuttonpress()
    plt.close()


if __name__ == "__main__":
    #
    NP = 20
    G = 200
    D = 20
    Size = 400
    GeneticAlg(NP, G, D, Size)