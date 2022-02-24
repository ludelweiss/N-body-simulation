# Projet de modélisation séance 2 - 10/02/22

import numpy as np
import matplotlib.pylab as plt


# Premier test avec deux corps de masses 1 :

# Variables
G=1
ma=1
mb=1

#nb d'objets :
N=2
#nb de coordonnées :
i=3

X=np.zeros((i,N))
X[0,1]=1    #positions initiales des particules A et B

V=np.zeros((i,N))
V[0,1]=1    #vitesse initiale des particules A et B


# Distance entre A et B :
def rab(X):
    rab=np.sqrt( (V[0,1]-V[0,0])**2 + (V[1,1]-V[1,0])**2 + (V[2,1]-V[2,0])**2 )
    rab=np.sqrt( np.sum((V[:,0]-V[:,1])**2) )
    return rab
    
# Norme de la force entre A et B en fonction de rab :
def Fab(rab):
    Fab=G*ma*mb*(1/rab**2)
    return Fab


t=0 #instant initial
dt=1 #pas de temps pour l'intégration
T=60 #intervalle d'intégration


# Calcul du dv ajouté à chaque dt pour A :
def fA(V, t):
    dV=np.zeros(3)
    dV[0]= Fab(rab(X))*t
    dV[1]= 0
    dV[2]= 0
    return dV


# Calcul du dv ajouté à chaque dt pour B :
def fB(V, t):
    dV=np.zeros(3)
    dV[0]= -Fab(rab(X))*t
    dV[1]= 0
    dV[2]= 0
    return dV



def euler(dt, X, V, N, i):
    
    #calcul du tableau des X pour A et B :
    tab_euler_X = np.zeros( (i,N) )
    for n in range(0,N):
        for i in range(0,i) :
            tab_euler_X[i,n]=X[i,n]+V[i,n]*dt

    print("tab des positions :",tab_euler_X)
    
    i=3
    tab_euler_V = np.zeros((i,N))
    #stockage des valeur de dV de A et B dans dV :
    dV= np.vstack((fA(V,dt),fB(V,dt))).T
    print("dv=",dV)
    
    i=3
    #stockage des valeurs de V pour A dans tab_euler_V :
    for i in range(0,i):
        tab_euler_V[i,0]=V[i,0]+dV[i,0]*dt
    
    i=3
    #stockage des valeurs de B dans tab_euler_V :
    for i in range(0,i):
        tab_euler_V[i,1]=V[i,1]+dV[i,1]*dt
    
    print("tab des vitesses :",tab_euler_V)

    return tab_euler_X , tab_euler_V

print(euler(dt,X,V,N,i))

"""
Creation des tableaux contenants les positions et vitesses
"""


tab_euler = euler(dt, X, V, N, i)
tab_euler_X = tab_euler[0]
tab_euler_V = tab_euler[1]
print("Les tableaux", tab_euler_X, tab_euler_V)


#for t in range(0,T,dt):
    #voir brouillon


