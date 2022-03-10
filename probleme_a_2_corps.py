"""
Modélisation des interactions entre deux particules (premier cas élémentaire) :
deux corps A et B de masse 1

Calcul des trajectoires uniquement

Séances 1, 2, 3, 4, 6

Auteurs : Ludmilla Allard et Annaëlle Sorce
"""

import numpy as np

# Premier test avec deux corps de masses 1 :

# Variables (choisies à 1 pour simplifier le problème)
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


'''
Méthodes d'intégration
'''
# Méthode d'intégration Euler
def euler(X, V, i, N, dt):
    tab_euler_X = X
    tab_euler_V = V
    
    #calcul du tableau des X pour A et B :
    for n in range(0,N):
        for i in range(0,i) :
            tab_euler_X[i,n]=tab_euler_X[i,n]+tab_euler_V[i,n]*dt
    
    #stockage des valeur de dV de A et B dans dV :
    dV= np.vstack((fA(V,dt),fB(V,dt))).T
    
    i=3
    #stockage des valeurs de V pour A dans tab_euler_V :
    for i in range(0,i):
        tab_euler_V[i,0]=tab_euler_V[i,0]+dV[i,0]*dt
    
    i=3
    #stockage des valeurs de B dans tab_euler_V :
    for i in range(0,i):
        tab_euler_V[i,1]=tab_euler_V[i,1]+dV[i,1]*dt
    
    i=3

    return tab_euler_X , tab_euler_V


#Méthode d'intégration Leapfrog
def leapfrog(X, V, i, N, dt) :
    tab_lf_X = X
    tab_lf_V = V
  



"""
Creation des tableaux contenants les positions et vitesses
"""

#Fonction pour stocker la position X et la vitesse V en iD de N particules à chaque instant dt jusqu'à T :
def mouvement(X,V,i,N,dt,T):
    NT = int(T/dt)
    #tableau de taille (N,i,dt) pour stocker les valeurs finales de X et V :
    VAL_X=np.zeros((i,N,NT))
    VAL_X[:,:,0]=X
    VAL_V=np.zeros((i,N,NT))
    VAL_V[:,:,0]=V
    for it in range(1, NT):
        tab_euler=euler(X,V,i,N,dt)
        VAL_X[:,:,it]=tab_euler[0]
        VAL_V[:,:,it]=tab_euler[1]   
    return VAL_X, VAL_V