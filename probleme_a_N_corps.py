"""
Modélisation d'un problème à N corps en avec la méthode des champs moyens

Séances 4

Auteurs : Ludmilla Allard et Annaëlle Sorce
"""

import numpy as np


N=6   #nombre de particules
dim=1   #dimension géométrique de la grille
nb_pt=10  #nombre de points sur une ligne de la grille
i=2   #dimension du problème
dx = dim/(nb_pt-1)   #distance entre deux points de la grille

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
print (Init(i,N,dim))

# Stockage des données initiales du problème :
Xi,Vi,M=Init(i, N, dim)


# Initialisation de la grille :

# Remplissage des potentiels de dimension i dans une grille de taille dim*dim :

def grille(Xi,M,nb_pt) :
    Grille=np.zeros((nb_pt,nb_pt))
    for x_g in range (0,nb_pt) :
        for y_g in range (0,nb_pt):
            for etoile in range (0,N):
                Grille[x_g, y_g] = Grille[x_g, y_g] + M[etoile] / np.sqrt(( Xi[0,etoile]-x_g )**2+ ( Xi[1,etoile]-y_g )**2)
                print("x_g=",x_g,"y_g=",y_g,"etoile=", etoile)
            print('\n',Grille,'\n')
                
    return Grille

#grille(Xi,M,nb_pt)
    

# Fonction permettant de calculer le gradient du potentiel en un point donné dans les limites de notre grille de potentiel :

def grad(f, X, etoile, dx) :
    
    coord = X[:,etoile]     # On récupère les coordonnées d'une particule N donnée dans notre tableau de valeurs X (à simplifier dans les boucles)
    
    O = np.int( (coord/dx) + (1/2) )    # On trouve le point le plus proche de notre étoile dans la grille
    
    # On approxime notre fonction par un polynôme de second ordre tel que
    # f(x_loc,y_loc) = a + b*x_loc + c*y_loc + d*x_loc*y_loc + e*(x_loc**2) + f*(y_loc**2)
    
    # Calcul des coef du polynôme :
    a = f[ O[0] , O[1] ]
    b = 0.5 * ( f[ O[0]+1 , O[1] ] - f[ O[0]-1 , O[1] ] )
    c = 0.5 * ( f[ O[0] , O[1]+1 ] - f[ O[0] , O[1]-1 ] )
    d = 0.25 * ( f[ O[0]+1 , O[1]+1 ] + f[ O[0]-1 , O[1]-1 ] ) - ( f[ O[0]-1 , O[1]+1 ] + f[ O[0]+1 , O[1]-1 ] )
    e = f[ O[0]-1 , O[1] ] + f[ O[0]+1 , O[1] ] - 2 * f[ O[0] , O[1] ]
    f = f[ O[0] , O[1]-1 ] + f[ O[0] , O[1]+1 ] - 2 * f[ O[0] , O[1] ]
    
    x_loc = (coord[0] - O[0]*dx)/dx
    y_loc = (coord[1] - O[1]*dx)/dx
    
    # On renvoie les valeurs du gradient :
    return ( b + 2*e*x_loc + d*y_loc , c+2*f*y_loc+d*x_loc )
 

#Méthode d'intégration Leapfrog
def leapfrog(X, V, i, N, dt) :
    X_demi = X + V*dt/2
    Grille = grille(X_demi, M, nb_pt)
    
    dV = np.zeros_like(V)
    for n1 in range(N) :
        dV[:,n1] = -dt*grad(Grille, X_demi, n1, dx)
    
    V_apres = V + dV
    
    X_apres = X_demi + V_apres*dt/2
    return X_apres , V_apres

