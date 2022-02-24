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
    tab_euler_X = np.zeros(i*N)
    for n in range(0,N):
        for i in range(0,i*N) :
            if (i<3):
                tab_euler_X[i]=X[i,n]+V[i,n]*dt
            if (i>=3):
                tab_euler_X[i]=X[i-3,n]+V[i-3,n]*dt
        i=3
    tab_euler_X=tab_euler_X.reshape((3,N))
    print("tab des positions :",tab_euler_X)
    
    i=3
    tab_euler_V = np.zeros(i*N)
    #stockage des valeur de dV de A et B dans dV :
    dV= np.vstack((fA(V,dt),fB(V,dt)))
    print("dv=",dV)
    
    i=3
    #stockage des valeurs de V pour A dans tab_euler_V :
    for i in range(0,i):
        tab_euler_V[i]=V[i,0]+dV[0,i]*dt
    
    i=3
    #stockage des valeurs de B dans tab_euler_V :
    for i in range(i,2*i):
        tab_euler_V[i]=V[i-3,1]+dV[1,i-3]*dt
    
    tab_euler_V=tab_euler_V.reshape(3,N)
    print("tab des vitesses :",tab_euler_V)

    return tab_euler_X , tab_euler_V

print(euler(dt,X,V,N,i))

# creation du tableau
tab_euler = euler(dt, X, V, N, i)
tab_euler_X = tab_euler[0]
tab_euler_V = tab_euler[1]
print("Les tableaux", tab_euler_X, tab_euler_V)


"""
interface graphique
"""

plt.plot(tab_euler_X, tab_euler_V, label = "Trajectoire des particules")
plt.xlabel("Position x")
plt.ylabel("Vitesse v")
plt.legend()
plt.show()