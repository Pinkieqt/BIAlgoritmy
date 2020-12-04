import numpy as np
import matplotlib.pyplot as plt
import math as m

def getFunctionZ(functionName, x, y):
    if functionName == "sphere":
        return SphereFunction(x, y)
    elif functionName == "schwefel":
        return SchwefelFunction(x, y)
    elif functionName == "griewank":
        return GriewankFunction(x, y)
    elif functionName == "rastrigin":
        return RastriginFunction(x, y)
    elif functionName == "lewy":
        return LevyFunction(x, y)
    elif functionName == "michalewitz":
        return MichalewitzFunction(x, y)
    elif functionName == "zakharov":
        return ZakharowFunction(x, y)
    elif functionName == "ackley":
        return AckleyFunction(x, y)

## Functions
def SphereFunction(x, y):
    dim = (x, y)
    result = 0.0
    for i in range(0,2):
        result += dim[i]**2

    return result

def SchwefelFunction(x, y):
    dim = (x,y)
    result = 0.0
    for i in range(0,2):
        result += dim[i] * np.sin(np.sqrt(abs(dim[i])))

    result = 418.9829 - result
    return result

def RosenbrockFunction(x, y):
    dim = (x,y)
    result = 0.0
    for i in range(0,2-1):
        temp = 100* (dim[i+1]-dim[i]**2)**2 + (1 -dim[i])**2
        result += temp

    return result    

def RastriginFunction(x, y):
    d = 2
    dim = (x, y)
    res = 0.0
    for i in range(0,d):
        res += 10 * d + dim[i]**2 - 10 * np.cos(2*np.pi * dim[i])

    return res

def LevyFunction(x, y):
    d = 2
    dim = (x, y)
    sum1 = []
    w1 = 1 + ((dim[d - 1] - 1) / 4)
    wd = 1 + ((dim[0] - 1) / 4)
    for i in range(0,d-1):
        wi = 1 + ((dim[i] - 1) / 4)
        
        sum1.append( (wi - 1)**2 * (1 + 10*np.sin(np.pi*wi+1)**2) + (wd-1)**2 * (1+np.sin(2*np.pi*wd)**2) )

    z = np.sin(np.pi*w1)**2 + sum(sum1)

    return z

def GriewankFunction(x, y):
    d = 2
    res = 0.0
    for i in range(1,d):
        tmp = (x*x + y*y)/4000
        tmpCos = np.cos(x) * np.cos(y) / np.sqrt(i)
        res += tmp + tmpCos + 1

    return res
    
def MichalewitzFunction(x, y):
    dim = (x, y)
    sum1=[]
    m = 10
    i = 1
    for val in dim:
        sum1.append(np.sin(val) * np.sin((i * val**2 ) / np.pi)**(2 * m))
        i = i + 1

    return - 1 * sum(sum1)

def ZakharowFunction(x, y):
    dim = (x, y)
    f=[]
    s=[]
    t=[]

    i = 1
    for el in dim:
        f.append(el**2)
        s.append(0.5*i*el)
        t.append(0.5*i*el)
        i = i + 1

    res = sum(f) + (sum(s))**2 + (sum(t))**4
    return res

def AckleyFunction(x, y):
    dim = (x, y)
    a = 20
    b = 0.2
    c = 2 * np.pi
    temp1 = []
    temp2 = []

    for el in dim:
        temp1.append(el**2)
        temp2.append(np.cos(c*el))
    


    temp11 = - a * np.exp(-b*np.sqrt(sum(temp1)/len(dim)))
    temp22 = np.exp(sum(temp2)/len(dim))

    res = temp11 - temp22 + a + np.exp(1)

    return res
