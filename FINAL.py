#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
FPT
"""

#Library
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#Variable
M=int(128)
theta = np.linspace(0, np.pi *2, M+1)[:-1]+0.1*np.pi/M
longueur=0.0
norme=0.0
time=0.0
dt = 5e-5

#width and height
#a=1.1
a=1.1
b=1.0

#Variable with the values of a and b

Xi =  a * np.cos(theta)
Yi =  b * np.sin(theta)
Zi = np.zeros(M)


T=np.zeros(3)
K = np.zeros(3)
N = 100000

Xc = np.copy(Xi)
Yc = np.copy(Yi)
Zc = np.copy(Zi)

X = np.copy(Xi)
Y = np.copy(Yi)
Z = np.copy(Zi)

## test tracer 
curv0 = np.zeros(N)
curv1 = np.zeros(N)
curv2 = np.zeros(N)
temp = np.zeros(N)
Kk0 = np.zeros(N)
Kk1 = np.zeros(N)
Kk2 = np.zeros(N)
courbure0 = np.zeros(N)
courbure1 = np.zeros(N)
courbure2 = np.zeros(N)
posx = np.zeros(M)
posy = np.zeros(M)
posz = np.zeros(M)
print(posx,posy,posz)
aba = 0
lg=np.zeros(N)
posmaxx = np.zeros(N)
posmaxy = np.zeros(N)
posmaxz = np.zeros(N)

for i in range(0,M):
                
        T[0] = (Xc[(i-2)%M]-8*Xc[(i-1)%M]+8*Xc[(i+1)%M]-Xc[(i+2)%M])/12
        T[1] = (Yc[(i-2)%M]-8*Yc[(i-1)%M]+8*Yc[(i+1)%M]-Yc[(i+2)%M])/12
        T[2] = (Zc[(i-2)%M]-8*Zc[(i-1)%M]+8*Zc[(i+1)%M]-Zc[(i+2)%M])/12
        
        norme = T[0]**2+T[1]**2+T[2]**2
        print(i)     
        longueur+=np.sqrt(norme) 
length=longueur

for t in range(0, N):
    
  
    time=time+dt
    longueur=0.0
    k= np.random.randint(0, M)
    Kb0 = [0,0,0] ##t
    K0 = [0,0,0] ##t
    for j in range(0,M):
        i=(k+j)%M        
        T[0] = (Xc[(i-2)%M]-8*Xc[(i-1)%M]+8*Xc[(i+1)%M]-Xc[(i+2)%M])/12
        T[1] = (Yc[(i-2)%M]-8*Yc[(i-1)%M]+8*Yc[(i+1)%M]-Yc[(i+2)%M])/12
        T[2] = (Zc[(i-2)%M]-8*Zc[(i-1)%M]+8*Zc[(i+1)%M]-Zc[(i+2)%M])/12
        
        norme = T[0]**2+T[1]**2+T[2]**2
        
        K[0] = (-Xc[(i-2)%M]+16*Xc[(i-1)%M]-30*Xc[(i+0)%M]+16*Xc[(i+1)%M]-Xc[(i+2)%M])/12
        K[1] = (-Yc[(i-2)%M]+16*Yc[(i-1)%M]-30*Yc[(i+0)%M]+16*Yc[(i+1)%M]-Yc[(i+2)%M])/12
        K[2] = (-Zc[(i-2)%M]+16*Zc[(i-1)%M]-30*Zc[(i+0)%M]+16*Zc[(i+1)%M]-Zc[(i+2)%M])/12
        
        Kb = np.cross(T,K)/norme**1.5
       
        X[i] = Kb[0] * dt + Xc[i]
        Y[i] = Kb[1] * dt + Yc[i]
        Z[i] = Kb[2] * dt + Zc[i]
             
        longueur+=np.sqrt(norme)
        
    
        posx[j] = X[i]
        posy[j] = Y[i]
        posz[j] = Z[i]
        
    temp[t] = t ##t
    posmaxx[t] = max(posx)
    posmaxy[t] = max(posy)
    posmaxz[t] = max(posz)
    print(t*dt) ##t
    print(longueur)
    lg[t] = longueur
    
    longueur=length/longueur
    X = X*longueur
    Y = Y*longueur
    Z = Z*longueur
  
    Xc = np.copy(X)
    Yc = np.copy(Y)
    Zc = np.copy(Z)


a3 = plt.figure()
plt.plot(temp[:70000]*dt,posmaxy[:70000],label='period = 45000')
plt.xlabel('time')
plt.ylabel('Y position')
plt.title('a=1.5 b=1.0')
plt.legend()
#a3.savefig("ab1012", format="pdf")

