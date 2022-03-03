"""
Modélisation d'un problème à N corps en avec la méthode des champs moyens

Séances 4

Auteurs : Ludmilla Allard et Annaëlle Sorce
"""

import numpy as np


N=30   #nombre de particules
dim=20   #dimension de la grille
i=3   #dimension du problème

#Initialisation des coordonnées de positions, de vitesses et de masse
# de N particules en dimension i réparties sur une grille carrée de dimension dim*dim :
    
def Initialisation(i,N,dim) :
    
    # Initialisation des positions :
    X=np.random.uniform(0,dim,N)
    for i in range(0,i-1):
        X=np.vstack((X,np.random.uniform(0,dim,N)))
    
    i=3
    # Initialisation des vitesses :
    V=np.random.normal(0,2.99792E8,N)
    for i in range(0,i-1):
        V=np.vstack((V,np.random.normal(0,3E8,N)))
    
    i=3
    # Initialisation des masses :
    M=np.random.uniform(2E30,300*2E30,N)
    
    return X,V,M

