#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
FPT
"""

#Library
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#Constantes de simulation
M=128
dt = 5e-5
N = 1000
TMAX = dt*N

## Configuration demi-axes initiale
a=1.5
b=1.0

## Dérivée seconde 
T=np.zeros(3)
## Rayon de courbure
K = np.zeros(3)

## Variables tampon
Xc = np.copy(Xi) ; Yc = np.copy(Yi) ; Zc = np.copy(Zi)
## Variables finales
X = np.copy(Xi) ; Y = np.copy(Yi) ; Z = np.copy(Zi)

### Définition des dérivées et rayons de courbure au point j dans l'axe Tab
def derivee(tab,j,taille):
    return (tab[(j-2)%taille]-8*tab[(j-1)%taille]+8*tab[(j+1)%taille]-tab[(j+2)%taille])/12
def courbure(tab,j,taille):
    return (-tab[(j-2)%taille]+16*tab[(j-1)%taille]-30*tab[(j+0)%taille]+16*tab[(j+1)%taille]-tab[(j+2)%taille])/12

#### Initialisation du vortex à T0
theta = np.linspace(0, np.pi *2, M+1)[:-1]+0.1*np.pi/M
Xi =  a * np.cos(theta) ; Yi =  b * np.sin(theta) ; Zi = np.zeros(M)

for i in range(0,M):
    T[0] = derivee(Xc,i,M)
    T[1] = derivee(Yc,i,M)
    T[2] = derivee(Zc,i,M)

### Simulations numériques pour N pas de temps ###
for t in range(0, N):
    #Tentative pour enlever la singularité à theta=0
    k= np.random.randint(0, M)
    # Boucle sur les angles
    for j in range(0,M):
        i=(k+j)%M        
        T[0] = derivee(Xc,i,M)
        T[1] = derivee(Yc,i,M)
        T[2] = derivee(Zc,i,M)
        K[0] = courbure(Xc,i,M)
        K[1] = courbure(Yc,i,M)
        K[2] = courbure(Zc,i,M)
        norme = T[0]**2+T[1]**2+T[2]**2
        Kb = np.cross(T,K)/norme**1.5
       
        X[i] = Kb[0] * dt + Xc[i]
        Y[i] = Kb[1] * dt + Yc[i]
        Z[i] = Kb[2] * dt + Zc[i]
  
    Xc = np.copy(X) ; Yc = np.copy(Y) ; Zc = np.copy(Z)
    
#    if t%1000 ==1 :
#        fig = plt.figure()
#        ax = fig.add_subplot(111, projection='3d')
#        ax.scatter(Z, Y, X)
#        #ax.plot(0,0,np.linspace(-10,100,100))
#        ax.axis([-0.02,0.25,-0.65,0.65])
#        #plt.axis([-1.1,1.1,-1.1,1.1])
#        #plt.axis('equal')
#        ax.legend()
#        plt.show()
#        print('t', time)
#        
#
#        a1 = plt.subplot(221)
#        a1.scatter(Z,0.3*X+0.3*Y,1)
#        a1.axis([-0.02,0.25,-0.65,0.65])
#        plt.xlabel('0.3x+0.3y')
#        plt.ylabel('z')
#        #plt.legend()
#        a1.set_title('z=f(0.3x+0.3*y)')
#
#        
#        a2 = plt.subplot(222)
#        a2.scatter(Z,X,1)
#        #a2.axis('equal')
#        a2.axis([-0.02,0.35,-2,2])
#        plt.xlabel('x')
#        plt.ylabel('z')
#        #plt.legend()
#        a2.set_title('z=f(x)')
#
#        a4 = plt.subplot(223)
#        a4.scatter(Z,Y,1)
#        #a4.axis([-0.05,0.05,-1.2,1.2])
#        a4.axis('equal')
#        plt.xlabel('y')
#        plt.ylabel('z')
#        #plt.legend()
#        a4.set_title('z=f(y)')
#        
#        a3 = plt.subplot(224)
#        a3.scatter(Y,X,2,label='ring')
#        a3.scatter(Yi,Xi,0.5,label='original shape')
#        a3.axis('equal')
#        plt.xlabel('x')
#        plt.ylabel('y')
#        plt.title('test')
#        plt.legend(loc=1, fontsize = 'x-small')
#        a3.set_title('y=f(x)')
#        
#        plt.tight_layout()
#        plt.show()
