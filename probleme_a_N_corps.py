"""
Modélisation d'un problème à N corps en avec la méthode des champs moyens

Séances 4e

Auteurs : Ludmilla Allard et Annaëlle Sorce
"""

import numpy as np
import matplotlib.pylab as plt
import matplotlib.cm as cm
import os
import shutil


N=80  #nombre de particules
dim=10   #dimension géométrique de la grille
nb_pt=8  #nombre de points sur une ligne de la grille
i=2   #dimension du problème
dx = dim/(nb_pt-1)   #distance entre deux points de la grille

T=4
dt=0.01

#Initialisation des coordonnées de positions, de vitesses et de masse
# de N particules en dimension i réparties sur une grille carrée de dimension dim*dim :
   
def Init(i,N,dim) :
   
    # Initialisation des positions :
    X=np.random.uniform(0.2*dim,0.8*dim,(i, N))
    
    # Initialisation des vitesses :
    V=np.random.normal(0,0.1,(i,N))
    #V=np.random.randint(0, 2, (i,N), dtype = int)
    
    # Initialisation des masses :
    M=np.random.uniform(0.2,10,N)
    return X,V,M

# Stockage des données initiales du problème :
Xi,Vi,M=Init(i, N, dim)


# Initialisation de la grille :

# Remplissage des potentiels de dimension i dans une grille de taille dim*dim :

def grille(Xi,M,nb_pt, dx) :
    Grille=np.zeros((nb_pt,nb_pt))
    for x_g in range (nb_pt) :
        for y_g in range (nb_pt):
            for etoile in range (0,N):
                Grille[x_g, y_g] -= M[etoile] / np.sqrt(( Xi[0,etoile]-x_g*dx )**2+ ( Xi[1,etoile]-y_g*dx )**2)
               
    return Grille

#grille(Xi,M,nb_pt)


# Fonction permettant de calculer le gradient du potentiel en un point donné dans les limites de notre grille de potentiel :

def grad(f, X, etoile, dx) :
   
    coord = X[:,etoile]     # On récupère les coordonnées d'une particule N donnée dans notre tableau de valeurs X (à simplifier dans les boucles)
    O=np.zeros(i,int)
    for y in range(i):
        O[y] = int( (coord[y]/dx) + (1/2) )    # On trouve le point le plus proche de notre étoile dans la grille
   
    if 0 < O[0] < nb_pt-1 and 0 < O[1] < nb_pt-1 :
        '''
        On approxime notre fonction par un polynôme de second ordre tel que :
        f(x_loc,y_loc) = a + b*x_loc + c*y_loc + d*x_loc*y_loc + e*(x_loc**2) + f*(y_loc**2)
        '''
   
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
        grad = np.array((b + 2*e*x_loc + d*y_loc , c+2*f*y_loc+d*x_loc))
        
    else :
        grad = np.zeros(i)

    
    return grad
 

#Méthode d'intégration Leapfrog
def leapfrog(X, V, i, N, dt) :
    X_demi = X + V*dt/2
    Grille = grille(X_demi, M, nb_pt, dx)
   
    dV = np.zeros_like(V)
    for n1 in range(N) :
        dV[:,n1] = -dt*grad(Grille, X_demi, n1, dx)
    
    V_apres = V + dV
    
    X_apres = X_demi + V_apres*dt/2
    return X_apres , V_apres

def mouvement_lf(i,N,dt,T):
    X,V,M=Init(i,N,dim)
    NT = int(T/dt)
    #tableau de taille (N,i,dt) pour stocker les valeurs finales de X et V :
    VAL_X=np.zeros((i,N,NT+1))
    VAL_X[:,:,0]=X
    VAL_V=np.zeros((i,N,NT+1))
    VAL_V[:,:,0]=V
    for it in range(1, NT+1):
        X,V=leapfrog(X,V,i,N,dt)
        VAL_X[:,:,it]=X
        VAL_V[:,:,it]=V
    return VAL_X, VAL_V


mvt = mouvement_lf(i,N,dt,T)
X = mvt[0][0]
Y = mvt[0][1]


'''
Boucle pour afficher les graphiques à chaque temps
'''
plt.style.use('dark_background')
try : 
    shutil.rmtree("Mvt-N-part_leapfrog")
except : pass
os.mkdir("Mvt-N-part_leapfrog")

cpt = 0 # décompte pour les numéros des graphiques
xgrille = np.linspace(0,dim,nb_pt)
color_max = 2*N

for t in range(1, int(T/dt)+1, 2) :
    
    x = X[:,t-1]
    y = Y[:,t-1]
    
    
    fig, ax = plt.subplots()
    
    ax.scatter(x,y, c = M, zorder = 3)
    ax.set(xlim=(0, dim), xticks=np.arange(0, dim+1),ylim=(0, dim), yticks=np.arange(0, dim+1))
    
    # affichage de la grille de potentiel
    ax.pcolormesh(xgrille, xgrille, grille(mvt[0][:,:,t-1], M, nb_pt, dx), cmap = cm.Greys, zorder = 2, shading = 'nearest', vmin = -color_max, vmax = color_max)
    
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title("Position des deux particules avec la méthode Leapfrog")
    plt.savefig('Mvt-N-part_leapfrog/mvt_N_particules_%03g.png'%cpt)
    cpt += 1


x = X[:,int(T/dt)]
y = Y[:,int(T/dt)]

fig, ax = plt.subplots()
    
ax.scatter(x,y, c = M, zorder = 3)
ax.set(xlim=(0, dim), xticks=np.arange(0, dim+1),ylim=(0, dim), yticks=np.arange(0, dim+1))

ax.pcolormesh(xgrille, xgrille, grille(mvt[0][:,:,int(T/dt)], M, nb_pt, dx), cmap = cm.Greys, zorder = 2, shading = 'nearest', vmin = -color_max, vmax = color_max)

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Position des deux particules avec la méthode Leapfrog")
plt.savefig('Mvt-N-part_leapfrog/mvt_N_particules_%03g.png'%(cpt+1))


# creation des vidéos
os.system("ffmpeg -y -r 10 -i Mvt-N-part_leapfrog/mvt_N_particules_%03d.png mvt-N-part_leapfrog.mp4")
shutil.rmtree("Mvt-N-part_leapfrog")