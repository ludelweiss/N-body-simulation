"""
Modélisation des interactions entre deux particules (premier cas élémentaire) :
deux corps A et B de masse 1

Calcul des trajectoires uniquement

Séances 1, 2, 3, 4, 6

Auteurs : Ludmilla Allard et Annaëlle Sorce
"""

import numpy as np

# Premier test avec deux corps de masses 1 :

# G choisie à 1 pour simplifier le problème
G=1

#nb d'objets :
N=2
#nb de coordonnées :
i=3

X=np.zeros((i,N))
X[0,1]=1    #positions initiales des particules A et B

V=np.zeros((i,N))
V[0,1]=1    #vitesse initiale des particules A et B

# masses :
m = np.ones(N)


'''
Méthodes d'intégration
'''
# Méthode d'intégration Euler
def euler(X, V, i, N, dt):
    X_apres = X + V*dt
    
    dV = np.zeros_like(V)
    for n1 in range(N) :
        for n2 in range(N) :
            if n1 == n2 :
                continue
            dV[:,n1] = dV[:,n1] + dt*G*m[n2]* (X[:,n2]-X[:,n1])/(np.sum((X[:,n2]-X[:,n1])**2)**1.5)

    return X_apres, V + dV



#Méthode d'intégration Leapfrog
def leapfrog(X, V, i, N, dt) :
    X_demi = X + V*dt/2
    
    dV = np.zeros_like(V)
    for n1 in range(N) :
        for n2 in range(N) :
            if n1 == n2 :
                continue
            dV[:,n1] = dV[:,n1] + dt*G*m[n2]* (X_demi[:,n2]-X_demi[:,n1])/(np.sum((X_demi[:,n2]-X_demi[:,n1])**2)**1.5)
    
    V_apres = V + dV
    
    X_apres = X_demi + V_apres*dt/2
    return X_apres , V_apres



"""
Creation des tableaux contenants les positions et vitesses
"""

#Fonction pour stocker la position X et la vitesse V en iD de N particules à chaque instant dt jusqu'à T :
def mouvement_euler(X,V,i,N,dt,T):
    NT = int(T/dt)
    #tableau de taille (N,i,dt) pour stocker les valeurs finales de X et V :
    VAL_X=np.zeros((i,N,NT))
    VAL_X[:,:,0]=X
    VAL_V=np.zeros((i,N,NT))
    VAL_V[:,:,0]=V
    for it in range(1, NT):
        X,V=euler(X,V,i,N,T/it)
        VAL_X[:,:,it]=X
        VAL_V[:,:,it]=V 
    return VAL_X, VAL_V


def mouvement_lf(X,V,i,N,dt,T):
    NT = int(T/dt)
    #tableau de taille (N,i,dt) pour stocker les valeurs finales de X et V :
    VAL_X=np.zeros((i,N,NT))
    VAL_X[:,:,0]=X
    VAL_V=np.zeros((i,N,NT))
    VAL_V[:,:,0]=V
    for it in range(1, NT):
        X,V=leapfrog(X,V,i,N,T/it)
        VAL_X[:,:,it]=X
        VAL_V[:,:,it]=V
    return VAL_X, VAL_V