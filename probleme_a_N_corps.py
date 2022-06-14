"""
Modélisation d'un problème à N corps en avec la méthode des champs moyens

Auteurs : Ludmilla Allard et Annaëlle Sorce
"""

import numpy as np
import matplotlib.pylab as plt
import matplotlib.cm as cm
import os
import shutil
import numba as nb


N=300  #nombre de particules
dim=20   #dimension géométrique de la grille
nb_pt=30  #nombre de points sur une ligne de la grille
i=2   #dimension du problème
dx = dim/(nb_pt-1)   #distance entre deux points de la grille
# on définit G=1

T=1
dt=0.0001
dt_video = 0.005

#Initialisation des coordonnées de positions, de vitesses et de masse
# de N particules en dimension i réparties sur une grille carrée de dimension dim*dim :
np.random.seed(1451451421)
    
def Init(i,N,dim) :
   
    # Initialisation des positions :
<<<<<<< HEAD
    X=np.random.normal(dim/2, dim/20, (i, N))
    """X1 = np.random.normal(dim/4, dim/20, (i,N/2))
    X2 = np.random.normal(3*dim/4, dim/20, (i,N/2))
    X = np.vstack((X1,X2))"""
=======
    # Modele avec un seul amas :
    #X=np.random.normal(dim/2, dim/20, (i, N))
    
    # Modele avec deux amas :
    X1 = np.random.normal(dim/4, dim/20, (i,int(N/2)))
    X2 = np.random.normal(3*dim/4, dim/20, (i,int(N/2)))
    X = np.hstack((X1, X2))
>>>>>>> 06c281e56fa2a4bdcbaeeffa8d40914101e45b20
    
    # Initialisation des masses :
    M=np.random.uniform(0.2 ,10, N)
    
    # Initialisation des vitesses :
    V=np.random.normal(0, 10., (i,N))
    V_cm = np.sum( M[np.newaxis,:]*V[:,:], axis=1) / np.sum( M )
    V -= V_cm[:,np.newaxis]
    
    return X,V,M

# Stockage des données initiales du problème :
Xi,Vi,M=Init(i, N, dim)


# Initialisation de la grille :

# Remplissage des potentiels de dimension i dans une grille de taille dim*dim :
@nb.njit
def grille(Xi,M,nb_pt, dx) :
    Grille=np.zeros((nb_pt,nb_pt))
    for x_g in range (nb_pt) :
        for y_g in range (nb_pt):
            for etoile in range (0,N):
                r = np.sqrt(( Xi[0,etoile]-x_g*dx )**2+ ( Xi[1,etoile]-y_g*dx )**2)
                if r > dx/5 :
                    Grille[x_g, y_g] -= M[etoile] / r
    #X_cm = np.sum( M[np.newaxis,:]*Xi[:,:], axis=1) / np.sum( M )     # coordonnées du centre de masse
    X_cm=np.zeros(2)
    X_cm[0]  = np.sum(M*Xi[0,:]) / np.sum( M )     # coordonnées du centre de masse           
    X_cm[1]  = np.sum(M*Xi[1,:]) / np.sum( M )     # coordonnées du centre de masse           
    return Grille,X_cm



# Fonction permettant de calculer le gradient du potentiel en un point donné dans les limites de notre grille de potentiel :
@nb.njit
def grad(f, X_cm, X, etoile, dx) :
   
    coord = X[:,etoile]     # On récupère les coordonnées d'une particule N donnée dans notre tableau de valeurs X (à simplifier dans les boucles)
    O=np.zeros(i,dtype=np.int64)
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
        d = 0.25 * (( f[ O[0]+1 , O[1]+1 ] + f[ O[0]-1 , O[1]-1 ] ) - ( f[ O[0]-1 , O[1]+1 ] + f[ O[0]+1 , O[1]-1 ] ))
        e = 0.5 * (f[ O[0]-1 , O[1] ] + f[ O[0]+1 , O[1] ]) - f[ O[0] , O[1] ]
        f = 0.5 * (f[ O[0] , O[1]-1 ] + f[ O[0] , O[1]+1 ]) - f[ O[0] , O[1] ]
       
        x_loc = (coord[0] - O[0]*dx)/dx
        y_loc = (coord[1] - O[1]*dx)/dx
        
        # On renvoie les valeurs du gradient :
        grad = np.array((b + 2*e*x_loc + d*y_loc , c+2*f*y_loc+d*x_loc))
        
    else :
        grad = np.sum( M ) / ( np.sum( (coord - X_cm )**2) )**1.5 * (coord-X_cm)  #gradient du potentiel calculé en fonction de la distance par rapport au centre de masse

    return grad
 

grille_fixe = grille(Xi,M,nb_pt, dx)

#Méthode d'intégration Leapfrog
@nb.njit
def leapfrog(X, V, i, N, dt) :
    X_demi = X + V*dt/2
    Grille, X_cm = grille(X_demi, M, nb_pt, dx)
    #Grille, X_cm = grille_fixe
   
    dV = np.zeros_like(V)
    for n1 in range(N) :
        dV[:,n1] = -dt*grad(Grille, X_cm, X_demi, n1, dx)
    
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
VX = mvt[1][0]
VY = mvt[1][1]

'''
Calcul de la conservation de l'énergie
'''

def energie(X, Y, VX, VY):
    E = np.zeros(X.shape[1])
    for p1 in range(N) :
        E += M[p1] * (VX[p1, :]**2 + VY[p1, :]**2) /2
        for p2 in range(p1) :
            E -= M[p1]*M[p2] / np.sqrt((X[p2, :]-X[p1, :])**2 + (Y[p2, :]-Y[p1, :])**2)
    return(E)

Energie = energie(X, Y, VX, VY)

#Tracé comparatif des conservations d'énergie
x = np.linspace(0, T, int(T/dt)+1)
plt.plot(x, Energie, label = "énergie avec Leapfrog")
plt.legend()
plt.title("Comparatif des énergies à N corps")
plt.savefig("Comparatif-énergies-N-corps.pdf")


'''
#Boucle pour afficher les graphiques à chaque temps
'''
plt.style.use('dark_background')

# supprime le document contenant les images s'il existe déjà
try : 
    shutil.rmtree("Mvt-N-part_leapfrog")
except : pass
# Creation du dossier contenant les images
os.mkdir("Mvt-N-part_leapfrog")

cpt = 0 # décompte pour les numéros des graphiques
xgrille = np.linspace(0,dim,nb_pt)
color_max = 2*N


for t in range(1, int(T/dt)+1, int(dt_video/dt)) :
    
    x = X[:,t-1]
    y = Y[:,t-1]
    
    fig, ax = plt.subplots()
    
    ax.scatter(x,y, s = M, c= M, zorder = 3)
    ax.set(xlim=(-dim/4, dim*1.25), ylim=(-dim/4, dim*1.25))
    
    # affichage de la grille de potentiel
    Grille, X_cm = grille(mvt[0][:,:,t-1], M, nb_pt, dx)
    ax.pcolormesh(xgrille, xgrille, Grille.T, cmap = cm.Greys, zorder = 2, shading = 'nearest', vmin = -color_max, vmax = color_max)
    ax.plot(X_cm[0], X_cm[1], 'rx', zorder=3)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title(f"dt={dt}")
    plt.savefig('Mvt-N-part_leapfrog/mvt_N_particules_%03g.png'%cpt,dpi=150)
    cpt += 1


x = X[:,int(T/dt)]
y = Y[:,int(T/dt)]

fig, ax = plt.subplots()
    
ax.scatter(x,y, c = M, zorder = 3)
ax.set(xlim=(0, dim), ylim=(0, dim))
Grille, X_cm = grille(mvt[0][:,:,int(T/dt)], M, nb_pt, dx)
ax.pcolormesh(xgrille, xgrille, Grille.T, cmap = cm.Greys, zorder = 2, shading = 'nearest', vmin = -color_max, vmax = color_max)

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title(f"dt={dt}")
plt.savefig('Mvt-N-part_leapfrog/mvt_N_particules_%03g.png'%(cpt+1),dpi=150)


# creation des vidéos
<<<<<<< HEAD
os.system("ffmpeg -y -r 10 -i Mvt-N-part_leapfrog/mvt_N_particules_%03d.png mvt-N-part_leapfrog.mp4")
shutil.rmtree("Mvt-N-part_leapfrog")
=======
os.system("ffmpeg -y -r 10 -i Mvt-N-part_leapfrog/mvt_N_particules_%03d.png mvt-N-part.mp4")
shutil.rmtree("Mvt-N-part_leapfrog")

>>>>>>> 06c281e56fa2a4bdcbaeeffa8d40914101e45b20
