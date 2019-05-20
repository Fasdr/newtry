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
    for j in range(1, m - 1):
        for i in range(1, j):
            if (np.sign(i * (j - i) * (m - j - 1))) == 1 :
                n[j][i] = (1-w)*s[j][i]+(w/(2*(a+b)))*(a*n[j-1][i]+b*n[j][i-1]+a*s[j+1][i]+b*s[j][i+1]+(h**2)*RightSide[j][i])
    return n

# residual method

def leftside(s):
    n = copy.deepcopy(s)
    for j in range(m):
        for i in range(j+1):
            if (np.sign(i * (j - i) * (m - j - 1))) == 1 :
                n[j][i] = (-b*(s[j-1][i]-2*s[j][i]+s[j+1][i])-a*(s[j][i-1]-2*s[j][i]+s[j][i+1]))/(h*h)
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
w = 2
d = 10**-10
m = 40
h = 1/(m-1)

Start = [[ (math.exp(i*h)*math.cos(j*h))*(1-(np.sign(i * (j - i) * (m - j - 1)))) + (np.sign(i * (j - i) * (m - j - 1)))  for i in range(j+1)]for j in range(m)]
RightSide = [[ (math.exp(i*h)*math.cos(j*h))*0.2 for i in range(j+1)]for j in range(m)]
RealSolution = [[ (math.exp(i*h)*math.cos(j*h)) for i in range(j+1)]for j in range(m)]


# residual method

#print(RealSolution)
#print(RightSide)
#print((leftside(RealSolution))[20][10])
#print(RightSide[20][10])

















# over-relaxation method 



n = 1    
      
FM = copy.deepcopy(Start)

SM = nextrelax(FM)

while (norm(mdif(SM,FM)) > d):
    n += 1
    SM, FM = nextrelax(SM) , SM
print(n,norm(mdif(SM,FM)))
print(n,norm(mdif(SM,RealSolution)))

k = math.floor(2*m/3)
z = math.floor(m/2)

print(SM[k][z]-RealSolution[k][z])


print((nextrelax(RealSolution))[k][z])
print(RealSolution[k][z])








