import numpy as np
import random
import matplotlib.pyplot as plt
import Functions
import Algorithms
import GeneticAlgorithm

#----------------------------------------------------------------------------------------------------------
#Plotting function - used to plot algorithm and functions in 3D
def PlotFunction(xDimension, yDimension, step, function, alg, animate, normalDistSize):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x = y = np.arange(xDimension, yDimension, step)
    X, Y = np.meshgrid(x, y)

    #Function plotting
    Z = np.array([Functions.getFunctionZ(function, x, y) for x,y in zip(np.ravel(X), np.ravel(Y))]) 
    Z = Z.reshape(X.shape)
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='cool', alpha=0.35)

    #Algorithm plotting
    #Hillclimb alg
    if alg == "hillclimb":
        lowerPoints = Algorithms.HillClimbAlg(xDimension, yDimension, function, ax)
        if animate == True:
            for i in range(len(lowerPoints)-1):
                scatterX = lowerPoints[i][0]
                scatterY = lowerPoints[i][1]
                scatterZ = lowerPoints[i][2]
                ax.scatter(scatterX, scatterY, scatterZ, color="black", alpha=0.3)
                plt.pause(0.3)
        else:
            for i in range(len(lowerPoints)-1):
                scatterX = lowerPoints[i][0]
                scatterY = lowerPoints[i][1]
                scatterZ = lowerPoints[i][2]
                ax.scatter(scatterX, scatterY, scatterZ, color="black", alpha=0.3)
    #blind search                
    elif alg == "blind":
        xs, ys, zs = Algorithms.BlindSearchAlg(xDimension, yDimension, function, ax)
        ax.scatter(xs, ys, zs, color="black", s=20, alpha=0.3)
        ax.scatter(xs[-1], ys[-1], zs[-1], color="red", s=40, alpha=1)

    #Simulated annealing
    elif alg == "sannealing":
        xs, ys, zs = Algorithms.SimulatedAnnealingAlg(500, 0.5, 0.95, normalDistSize, xDimension, yDimension, function, ax)


    plt.show()


if __name__ == "__main__":

    ## Animate hillclimb?
    animate = True

    ## Algorithm to use
    #algorithm = ""
    #algorithm = "blind"
    #algorithm = "hillclimb"
    algorithm ="sannealing"


    #Sphere function
    #PlotFunction(-5.12, 5.12, 0.25, "sphere", algorithm, animate, 0.8)

    #Schwefel function
    #PlotFunction(-500, 500, 15, "schwefel", algorithm, animate, 30)

    #Griewank -
    #PlotFunction(-600, 600, 10, "griewank",algorithm, animate, 30)

    #Rastrigin
    #PlotFunction(-5.12, 5.12, 0.25, "rastrigin", algorithm, animate, 0.9)

    #Lewy
    #PlotFunction(-10, 10, 0.25, "lewy", algorithm, animate, 0.8)

    #Michalewitz
    #PlotFunction(0, np.pi, 0.05, "michalewitz", algorithm, animate, 1)

    #Zakharov
    #PlotFunction(-5, 10, 0.5, "zakharov", algorithm, animate, 4)

    #Ackley -32.768 až 32.768
    #PlotFunction(-5.768, 5.768, 0.1, "ackley", algorithm, animate, 1.5)

