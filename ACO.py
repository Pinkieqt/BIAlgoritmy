import numpy as np
import matplotlib.pyplot as plt
import copy
import random
import math

# Global variables
NUM_CITIES = 20
NUM_ANTS = 20
NUM_ITERATIONS = 20
EVAPORATION = 0.5
SIZE = 400

# City class
class City:
    def __init__(self, id, x, y, distances):
        self.id = id
        self.x = x
        self.y = y
        self.distances = distances
        self.pheromone = 1 # initial pheromone matrix like

# Ant class
class Ant:
    def __init__(self, id, city, route, routeLength):
        self.id = id
        self.initialCity = city
        self.currentCity = city
        self.route = route
        self.routeLength = routeLength

# Distance class
class Dist:
    def __init__(self, idOfCity, distanceFromTo, Pheromone, d):
        self.idOfCity = idOfCity
        self.dist = distanceFromTo
        self.pheromone = Pheromone
        self.visibility = d

# Generate cities
def GenerateCities():
    cities = []
    for i in range(NUM_CITIES):
        rndX = random.randint(0, SIZE)
        rndY = random.randint(0, SIZE)
        cities.append(City(i, rndX, rndY, []))
    
    # Calculate distances to other cities
    for currcity in cities:
        distances = []
        for city in cities:
            if (currcity.id == city.id): distances.append(Dist(city.id, 0, 1, 0))
            else:
                length = math.sqrt((currcity.x - city.x)**2 + (currcity.y - city.y)**2)
                distances.append(Dist(city.id, length, 1, 1/length)) #cityid, route lenght, initial pheromone, 1/d(r,s)
        currcity.distances = distances
        
    return cities

# Generate individual travelers
def GenerateAnts(allCities):
    individuals = []
    tmpCities = copy.deepcopy(allCities)
    #Generate NP individuals
    for i in range(NUM_ANTS):
        rnd = np.random.randint(0, len(tmpCities))
        initialCity = tmpCities.pop(rnd)
        tmpAnt = Ant(i, initialCity, [initialCity.id], 0.0)
        individuals.append(tmpAnt)

    return individuals

# Function which returns if ant already visited parameter's city
def WasVisited(ant, city):
    visited = False
    for entry in ant.route:
        if (entry == city.id):
            visited = True
    
    return visited

# Calculate possibility to visit other city
def CalculatePossibility(ant, cities):
    citiesToVisit = []
    probabilitySum = 0
    for city in cities:
        # If same city we dont have anything to count
        if (ant.currentCity.id == city.id or ant.initialCity == city.id): continue
        
        # Get distance from ANT to cities[i]
        distance = city.distances[ant.currentCity.id].dist

        # If already visited -> then we dont have anything to count again
        if (WasVisited(ant, city)):
            continue
        
        # Count probability, add it to "matrix" and then add it to probability sum
        probability = city.distances[ant.currentCity.id].pheromone ** 1 * city.distances[ant.currentCity.id].visibility ** 2
        citiesToVisit.append([city, probability])
        probabilitySum = probabilitySum + probability
    
    # If we still have somewhere to go
    if probabilitySum > 0:
        for entry in citiesToVisit:
            entry[1] = entry[1] / probabilitySum


    return citiesToVisit

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
def PlotRoute(route, cities):
    x = []
    y = []
    for i in range(len(route)):
        x.append(cities[route[i]].x)
        y.append(cities[route[i]].y)
    
    # get back to the starting city
    x.append(cities[route[0]].x)
    y.append(cities[route[0]].y)

    return x, y

# ACO
def ACO():
    #Graph
    plt.ion()
    fig = plt.figure()
    fig.suptitle("ACO")
    ax = fig.add_subplot()

    #Generate cities
    print("Generating cities")
    cities = GenerateCities()

    #Generate first population and evaulate first population
    print("Generating population")
    population = GenerateAnts(cities)

    lowestDist = None
    lowestRoute = None
    print("Finding the best solution.......... ")
    for i in range(NUM_ITERATIONS):
        if(i > 0): print("Iteration: " + str(i + 1) + ", distance: " + str(lowestDist))
        
        # Move ant
        for x in range(0, len(cities)):
            for ant in population:
                citiesToVisit = CalculatePossibility(ant, cities)
                
                if (len(citiesToVisit) == 0): 
                    # Include route back to initial city
                    ant.routeLength = ant.routeLength + ant.initialCity.distances[len(ant.route) - 1].dist

                else:
                    rnd = np.random.uniform()
                    probSum = 0
                    for entry in citiesToVisit:
                        # Cumulative probability
                        probSum = probSum + entry[1]
                        # if probability sum is bigger than random generated number then add this city to route
                        if (rnd <= probSum):
                            ant.route.append(entry[0].id)
                            ant.routeLength = ant.routeLength + entry[0].distances[ant.currentCity.id].dist
                            ant.currentCity = entry[0]
                            break
                

        # Calculate evaporation + find best ant (best route)
        deltaPheromone = 0
        routeLen = None
        tmpRoute = None
        for ant in population:
            deltaPheromone = deltaPheromone + (1 / ant.routeLength)
            if(routeLen == None): 
                routeLen = ant.routeLength
                tmpRoute = ant.route
            if(ant.routeLength < routeLen): 
                routeLen = ant.routeLength
                tmpRoute = ant.route
            
        for city in cities:
            city.pheromone = (1 - EVAPORATION) * city.pheromone + deltaPheromone


        # Is best overall?
        if(lowestDist == None): 
            lowestDist = routeLen
            lowestRoute = tmpRoute
        if(routeLen < lowestDist): 
            lowestDist = routeLen
            lowestRoute = tmpRoute
            
        # New population
        population = GenerateAnts(cities)

        if(i == 0): print("Iteration: " + str(i + 1) + ", distance: " + str(lowestDist))

        #Plot route
        plt.cla()
        PlotCities(cities, ax)
        x, y = PlotRoute(lowestRoute, cities)
        lengthText = "Vzdálenost trasy: " + str(round(lowestDist, 2))
        plt.plot(x, y, color="red", alpha=0.5, linewidth=1)
        plt.xlabel(lengthText, color="red")
        plt.pause(0.0000001)
        plt.draw()


    #After loop show graph
    print("Found!")
    print("Press any keyboard to close graph.")
    plt.show()   
    plt.waitforbuttonpress()
    plt.close()


if __name__ == "__main__":
    ACO()