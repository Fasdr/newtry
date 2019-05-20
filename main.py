import copy
import math
import numpy as np

# global functions

def product(s1, s2):
    prsum = 0
    for j in range(m):
        for i in range(j+1):
            prsum += h*h * s1[j][i] * s2[j][i]
    return prsum












#over-relaxation method

def nextrelax(s):
    n = copy.deepcopy(s)
    for j in range(m):
        for i in range(j + 1):
            if (np.sign(i * (j - i) * (m - j - 1))) == 1 :
                n[j][i] = 1/(2*w*(a+b)) * ( a * n[j][i-1] + b * n[j-1][i] + h*h*w*RigihtSide[j][i] + (w*b*s[j+1][i] + w*a*s[j][i+1] + (1-w)*b*s[j-1][i] + (1-w)*a*s[j][i-1] ) )
    return n





a = 1
b = 1.2
w = 1.1
m = 5 # будет m + 1 точка
h = 1/(m-1)

Start = [[ (math.exp(i*h)*math.cos(j*h))*(1-(np.sign(i * (j - i) * (m - j - 1)))) + (np.sign(i * (j - i) * (m - j - 1)))  for i in range(j+1)]for j in range(m)]
RigihtSide = [[ (math.exp(i*h)*math.cos(j*h))*0.2 for i in range(j+1)]for j in range(m)]
RealSolution = [[ (math.exp(i*h)*math.cos(j*h)) for i in range(j+1)]for j in range(m)]
