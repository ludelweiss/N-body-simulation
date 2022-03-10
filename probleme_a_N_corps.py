"""
Modélisation d'un problème à N corps en avec la méthode des champs moyens

Séances 4

Auteurs : Ludmilla Allard et Annaëlle Sorce
"""

import numpy as np


N=30   #nombre de particules
dim=20   #dimension de la grille
i=2   #dimension du problème

#Initialisation des coordonnées de positions, de vitesses et de masse
# de N particules en dimension i réparties sur une grille carrée de dimension dim*dim :
    
def Initialisation(i,N,dim) :
    
    # Initialisation des positions :
    X=np.sort(np.random.uniform(0,dim,N))
    for j in range(0,i-1):
        X=np.vstack((X,np.sort(np.random.uniform(0,dim,N))))
        print('boucle numéro', i, X)
    
    # Initialisation des vitesses :
    V=np.sort(np.random.normal(0,0.08*3E8,N))
    for j in range(0,i-1):
        V=np.vstack((V,np.random.normal(0,0.08*3E8,N)))
    
    # Initialisation des masses :
    M=np.random.uniform(0.07*2E30,300*2E30,N)
    
    return X,V,M

# Stockage des données initiales du problème :
Init=Initialisation(i, N, dim)
Xi=Init[0]
Vi=Init[1]
M=Init[2]

# Initialisation de la grille :
Grille=np.zeros((dim,dim)) 

# Calcul du potentiel en chaque point de la grille :
w=np.zeros(0,i)
for xg in range (0,dim-1) :
    for yg in range (0,dim-1):
        for etoile in range (0,N-1):
            w+=M[etoile]/()
        Grille[xg,yg]=sum(M[etoile]/())

