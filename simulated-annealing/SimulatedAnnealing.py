import numpy as np
import matplotlib.pyplot as plt
import math
import random

def function (x1,x2):
    f = (-(abs(math.sin(x1)*math.cos(x2)*math.exp(abs(1-(math.sqrt(math.pow(x1,2)+math.pow(x2,2))/3.14))))))
    return f

def fgetrand1 ():
    return random.uniform(-10,10)

def fgetrand2 ():
    return random.uniform(0,1)

x1 = fgetrand1()
x2 = fgetrand1()
tempEval = function(x1,x2)
T = 10000
while T>0.01 :
    for i in range(10000) :
        a = fgetrand1()
        b = fgetrand1()
        newEval = function(a,b)
        if tempEval>function(x1,x2):
            x1 = a
            x2 = b
            tempEval = newEval
        else : 
            delta = function(a,b) - function(x1,x2)
            if math.exp(-delta/T)>fgetrand2():
                x1 = a
                x2 = b
                tempEval = newEval
    T = 0.9*T
print("x1 : {}, x2 : {}" .format(x1, x2))
print("Best So Far : " + str(tempEval))


a = (abs((tempEval-19.2)/19.2))
g = (1-a)*-100
print (str(g)+"%")