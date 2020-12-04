import numpy as np
import Functions
import matplotlib.pyplot as plt
import random
import math

#----------------------------------------------------------------------------------------------------------
## blind search alg
def BlindSearchAlg(X, Y, func, ax):
    x = X
    y = Y
    z = Functions.getFunctionZ(func, x, y)
    globalMinFound = False

    maxIterations = 5000
    counter = 0

    xs = [x]
    ys = [y]
    zs = [z]

    while globalMinFound == False:
        gx = random.uniform(X, Y)
        gy = random.uniform(X, Y)
        gz = Functions.getFunctionZ(func, gx, gy)
        counter += 1

        if gz < z:
            z = gz
            xs.append(gx)
            ys.append(gy)
            zs.append(gz)

        if counter >= maxIterations:
            ax.scatter(xs[-1], ys[-1], zs[-1], color="r", s=40)
            globalMinFound = True
        
    return xs, ys, zs



#----------------------------------------------------------------------------------------------------------
## hill climb alg
def getLowestNeighbour(initX, initY, initZ, functionName):
    lowestX = 0
    lowestY = 0
    lowestZ = initZ
    coordinates =  np.random.multivariate_normal((initX, initY),[[1,0],[0 ,100]],10)
    #coordinates =  np.random.normal([initX, initY], 10)
    for i in range(len(coordinates)):
        tmp = Functions.getFunctionZ(functionName, coordinates[i][0], coordinates[i][1])
        if  tmp < lowestZ:
            lowestX = coordinates[i][0]
            lowestY = coordinates[i][1]
            lowestZ = tmp
    return lowestX, lowestY, lowestZ


def HillClimbAlg(x, y, functionName, ax):  

    lowerPoints = []

    # GENERATE SOLUTION
    initX = x
    initY = y
    initZ = Functions.getFunctionZ(functionName, initX, initY)
    globalMinFound = False

    max_iterations = 500
    counter = 0
        
    while globalMinFound == False:
        counter +=1
        # Generování sousedů a získání nejnižšího souseda
        lowestX, lowestY, lowestZ = getLowestNeighbour(initX, initY, initZ, functionName)
        
        if lowestZ < initZ and (lowestX >= x and lowestX <= y) and (lowestY >= x and lowestY <= y):
            # jestliže nejmenší je stejný jako již současný nejmenší

            print("Lower point :" + str(lowestZ))
            lowerPoints.append([lowestX, lowestY, lowestZ])
            #ax.scatter(lowestX, lowestY, lowestZ, color="k", s=20)

            if max_iterations < counter or (initX == lowestX and initY == lowestY):
                globalMinFound = True
                print("Max iterations done - minimum found") 
                print(lowestZ)           
                ax.scatter(lowestX, lowestY, lowestZ,color="r",s=40)
            else:
                initX = lowestX
                initY = lowestY
                initZ = lowestZ

    return lowerPoints

#----------------------------------------------------------------------------------------------------------
## simulated annealing algorithm
# t0 = initial temperature (100, 200...)
# tmin = minimal temperature (values close to 0)
# alfa = cooling constant (between 0 and 1 -> usually from 0.9 to 0.99)
def SimulatedAnnealingAlg(t0, tmin, alfa, normalDistSize, x, y, function, ax):
    T = t0

    #initial solution
    initX = x
    initY = y
    initZ = Functions.getFunctionZ(function, initX, initY)
    lowest = [initX, initY, initZ]

    while (T > tmin):
        # generování random
        newX = np.random.normal(initY, normalDistSize)
        newY = np.random.normal(initX, normalDistSize)
        newZ = Functions.getFunctionZ(function, newX, newY)

        ## pokud je mimo meze X a Y tak hned vyhodit jknak příjmout
        if (newZ < initZ and ((newX > x and newX < y) and (newY > x and newX < y))):
            initX = newX
            initY = newY
            initZ = newZ
            ax.scatter(initX, initY, initZ, color="black", s=20, alpha=0.3)
            print(initZ)
        else:
            r = np.random.uniform(0, 1)

            if (r < np.e**(-(newZ - initZ) / T) and ((newX > x and newX < y) and (newY > x and newX < y))):
                initX = newX
                initY = newY
                initZ = newZ
                ax.scatter(initX, initY, initZ, color="black", s=20, alpha=0.3)
                print(initZ)
        
        if (lowest[2] > initZ):
            lowest = [initX, initY, initZ]

        T = T * alfa

    print(lowest)

    #vykreslit nejmenší nalezený
    ax.scatter(lowest[0], lowest[1], lowest[2], color="r", s=40)

    return initX, initY, initZ


