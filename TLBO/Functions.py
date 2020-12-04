import numpy as np
import matplotlib.pyplot as plt
import math as m

def getFunctionZ(functionName, dim, data):
    if functionName == "sphere":
        return SphereFunction(dim, data)
    elif functionName == "schwefel":
        return SchwefelFunction(dim, data)
    elif functionName == "griewank":
        return GriewankFunction(dim, data)
    elif functionName == "rastrigin":
        return RastriginFunction(dim, data)
    elif functionName == "lewy":
        return LevyFunction(dim, data)
    elif functionName == "michalewitz":
        return MichalewitzFunction(dim, data)
    elif functionName == "zakharov":
        return ZakharowFunction(dim, data)
    elif functionName == "ackley":
        return AckleyFunction(dim, data)

## Functions
def SphereFunction(dim, data):
    result = 0.0
    for i in range(dim):
        result += data[i]**2

    return result

def SchwefelFunction(dim, data):
    result = 0.0
    for i in range(dim):
        result += data[i] * np.sin(np.sqrt(abs(data[i])))

    result = 418.9829 - result
    return result

def RosenbrockFunction(dim, data):
    result = 0.0
    for i in range(dim):
        temp = 100* (data[i+1]-data[i]**2)**2 + (1 -data[i])**2
        result += temp

    return result    

def RastriginFunction(dim, data):
    d = 2
    res = 0.0
    for i in range(dim):
        res += 10 * d + data[i]**2 - 10 * np.cos(2*np.pi * data[i])

    return res

def LevyFunction(dim, data):
    d = 2
    sum1 = []
    w1 = 1 + ((data[d - 1] - 1) / 4)
    wd = 1 + ((data[0] - 1) / 4)
    for i in range(dim):
        wi = 1 + ((data[i] - 1) / 4)
        
        sum1.append( (wi - 1)**2 * (1 + 10*np.sin(np.pi*wi+1)**2) + (wd-1)**2 * (1+np.sin(2*np.pi*wd)**2) )

    z = np.sin(np.pi*w1)**2 + sum(sum1)

    return z

def GriewankFunction(dim, data):
    sumdata = 0
    adddata = 1
    res = 0.0

    for i in range(dim):
        sumdata = sumdata + ((data[i] * data[i]))
        adddata = adddata * np.cos(data[i])

    tmp = sumdata / 4000
    tmpCos = adddata / np.sqrt(i)
    res += tmp + tmpCos + 1

    return res
    
def MichalewitzFunction(dim, data):
    sum1=[]
    m = 10
    i = 1
    for x in range(dim):
        sum1.append(np.sin(data[x]) * np.sin((i * data[x]**2 ) / np.pi)**(2 * m))
        i = i + 1

    return - 1 * sum(sum1)

def ZakharowFunction(dim, data):
    f=[]
    s=[]
    t=[]

    i = 1
    for x in range(dim):
        f.append(data[x]**2)
        s.append(0.5*i*data[x])
        t.append(0.5*i*data[x])
        i = i + 1

    res = sum(f) + (sum(s))**2 + (sum(t))**4
    return res

def AckleyFunction(dim, data):
    a = 20
    b = 0.2
    c = 2 * np.pi
    temp1 = []
    temp2 = []

    for x in range(dim):
        temp1.append(data[x]**2)
        temp2.append(np.cos(c*data[x]))
    


    temp11 = - a * np.exp(-b*np.sqrt(sum(temp1)/len(data)))
    temp22 = np.exp(sum(temp2)/len(data))

    res = temp11 - temp22 + a + np.exp(1)

    return res
