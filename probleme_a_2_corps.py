# Projet de modélisation séance 2 - 10/02/22

import numpy as np


# Premier test avec deux corps de masses 1 :

# Variables
G=1
ma=1
mb=1

N=2
i=3

X=np.zeros((i,N))
X[0,1]=1

V=np.zeros((i,N))
V[0,1]=1

'''
Norme des vitesses :
va=np.sqrt(V[0,0]**2+V[1,0]**2+V[2,0]**2)
vb=np.sqrt(V[0,1]**2+V[1,1]**2+V[2,1]**2)

Energie cinétique :
Ecb=0.5*mb*vb**2
'''

# Distance entre A et B :
def rab(X):
    rab=np.sqrt( (V[0,1]-V[0,0])**2 + (V[1,1]-V[1,0])**2 + (V[2,1]-V[2,0])**2 )
    return rab
    
# Norme de la force entre A et B en fonction de rab :
def Fab(rab):
    Fab=G*ma*mb*(1/rab**2)
    return Fab


t=0
dt=0.001


# Calcul du dv ajouté à chaque dt pour A :
def fA(V, t):
    dV=np.zeros(3)
    dV[0]=Fab(rab(X))*t
    dV[1]=0
    dV[2]=0
    return dV


# Calcul du dv ajouté à chaque dt pour B :
def fB(V, t):
    dV=np.zeros(3)
    dV[0]=-Fab(rab(X))*t
    dV[1]=0
    dV[2]=0
    return dV


N=2
i=3


dV= np.vstack((fA(V,dt),fB(V,dt)))
print(dV)

def eulerA(dt, X, V, N, i):
    tab_euler_X = np.zeros(3*N)
    
    for i in range(0,i) :
        tab_euler_X[0]=X[0,0]+V[0,0]*dt
        tab_euler_X[1]=X[1,0]+V[1,0]*dt
        tab_euler_X[2]=X[2,0]+V[2,0]*dt
    
    tab_euler_V = np.zeros(3*N)
    dV= np.vstack((fA(V,dt),fB(V,dt)))
    
    tab_euler_V[0]=V[0,0]+dVA[0]*dt
    tab_euler_V[1]=V[1,0]+dVA[1]*dt
    tab_euler_V[2]=V[2,0]+dVA[2]*dt
    
    
    tab_euler_V[3]=V[0,1]+dVB[0]*dt
    tab_euler_V[4]=V[1,1]+dVB[1]*dt
    tab_euler_V[5]=V[2,1]+dVB[3]*dt
    
    return tab_euler


# def Euler pour A :
def eulerA(dt, X, V):
    tab_euler = np.zeros(6)
    tab_euler[0]=X[0,0]+V[0,0]*dt
    tab_euler[1]=X[1,0]+V[1,0]*dt
    tab_euler[2]=X[2,0]+V[2,0]*dt
    tab_euler[3]=V[0,0]+fA1(V[0,0],dt)*dt
    tab_euler[4]=V[1,0]+fA2(V[1,0],dt)*dt
    tab_euler[5]=V[2,0]+fA3(V[2,0],dt)*dt
    return tab_euler

# def Euler pour B :
def eulerB(dt, X, V):
    tab_euler = np.zeros(2)
    tab_euler[0]=X[0,1]+V[0,1]*dt
    tab_euler[1]=X[1,1]+V[1,1]*dt
    tab_euler[2]=X[2,1]+V[2,1]*dt
    tab_euler[3]=V[0,1]+fB1(V[0,1],dt)*dt
    tab_euler[4]=V[1,1]+fB2(V[1,1],dt)*dt
    tab_euler[5]=V[2,1]+fB3(V[2,1],dt)*dt
    return tab_euler



