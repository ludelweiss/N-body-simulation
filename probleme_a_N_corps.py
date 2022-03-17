"""
Modélisation d'un problème à N corps en avec la méthode des champs moyens

Séances 4

Auteurs : Ludmilla Allard et Annaëlle Sorce
"""

import numpy as np


N=6   #nombre de particules
dim=3   #dimension de la grille
i=2   #dimension du problème

#Initialisation des coordonnées de positions, de vitesses et de masse
# de N particules en dimension i réparties sur une grille carrée de dimension dim*dim :
    
def Init(i,N,dim) :
    
    # Initialisation des positions :
    X=np.sort(np.random.uniform(0,dim,N))
    for j in range(0,i-1):
        X=np.vstack((X,np.random.uniform(0,dim,N)))
    
    # Initialisation des vitesses :
    V=np.random.normal(0,0.08*3E8,N)
    for j in range(0,i-1):
        V=np.vstack((V,np.random.normal(0,0.08*3E8,N)))
    
    # Initialisation des masses :
    M=np.random.uniform(0.07*2E30,300*2E30,N)
    
    return X,V,M

# Stockage des données initiales du problème :
Xi,Vi,M=Init(i, N, dim)


# Initialisation de la grille :

# Remplissage des potentiels de dimension i dans une grille de taille dim*dim :

def grille(Xi,M,dim) :
    Grille=np.zeros((dim,dim))
    for x_g in range (0,dim) :
        for y_g in range (0,dim):
            for etoile in range (0,N):
                Grille[x_g, y_g] = Grille[x_g, y_g] + M[etoile] / np.sqrt(( Xi[0,etoile]-x_g )**2+ ( Xi[1,etoile]-y_g )**2)
                print("x_g=",x_g,"y_g=",y_g,"etoile=", etoile)
            print('\n',Grille,'\n')
                
    return Grille

def accel (Pot, dx, x) :
    ix = int(x[0]/dx)
    iy = int(x[1]/dx)
    ax = ( Pot[ix+1, iy] - Pot[ix, iy] )/dx
    ay = ( Pot[ix, iy+1] - Pot[ix, iy]  )/dx
    

grille(Xi,M,dim)

