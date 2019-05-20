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

def norm(s):
    return math.sqrt(product(s, s))

def mdif(s1, s2):
    n = copy.deepcopy(s1)
    for j in range(m):
        for i in range(j+1):
            n[j][i] -= s2[j][i]
    return n

def mults(k,s):
    n = copy.deepcopy(s)
    for j in range(m):
        for i in range(j+1):
            n[j][i] = k * s[j][i]
    return n





# over-relaxation method

def nextrelax(s):
    n = copy.deepcopy(s)
    for j in range(m):
        for i in range(j + 1):
            if (np.sign(i * (j - i) * (m - j - 1))) == 1 :
                n[j][i] = 1/(2*w*(a+b)) * ( a * n[j][i-1] + b * n[j-1][i] + h*h*w*RigihtSide[j][i] + (w*b*s[j+1][i] + w*a*s[j][i+1] + (1-w)*b*s[j-1][i] + (1-w)*a*s[j][i-1] ) )
    return n

# residual method

def leftside(s):
    n = copy.deepcopy(s)
    for j in range(m):
        for i in range(j+1):
            if (np.sign(i * (j - i) * (m - j - 1))) == 1 :
                n[j][i] = -b*(s[j-1][i]-2*s[j][i]+s[j+1][i])-a*(s[j][i-1]-2*s[j][i]+s[j][i+1])/(h*h)
            else :
                n[j][i] = 0                
    return n

def inmdif(s1, s2):
    n = copy.deepcopy(s1)
    for j in range(m):
        for i in range(j+1):
            if (np.sign(i * (j - i) * (m - j - 1))) == 1 :
                n[j][i] -= s2[j][i]
            else :
                n[j][i] = 0
    return n







b = 1.2
a = 1
w = 1.5
d = 10**-6
m = 5
h = 1/(m-1)

Start = [[ (math.exp(i*h)*math.cos(j*h))*(1-(np.sign(i * (j - i) * (m - j - 1)))) + (np.sign(i * (j - i) * (m - j - 1)))  for i in range(j+1)]for j in range(m)]
RigihtSide = [[ (math.exp(i*h)*math.cos(j*h))*0.2 for i in range(j+1)]for j in range(m)]
RealSolution = [[ (math.exp(i*h)*math.cos(j*h)) for i in range(j+1)]for j in range(m)]


# residual method


print(leftside(RealSolution))
print(inmdif(leftside(RealSolution),RigihtSide))


















# over-relaxation method 

#print(Start)
#print(RealSolution)
#print(nextrelax(RealSolution))



#n = 1    
#      
#FM = copy.deepcopy(Start)
#
#SM = nextrelax(FM)
#
#while (norm(mdif(SM,FM)) > d):
##    print(n,norm(mdif(SM,FM)))
#    n += 1
#    SM, FM = nextrelax(SM) , SM
#print(n,norm(mdif(SM,FM)))
##print((mdif(SM,RealSolution)))
#print(n,norm(mdif(SM,RealSolution)))











