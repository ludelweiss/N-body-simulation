"""
Modélisation à l'aide d'une interface graphique du problème à 2 corps
Un graphique des positions est tracé pour chaque temps dt donné,
et les graphiques sont assemblés pour obtenir une vidéo du mouvement

Séances 3 et 4

Auteurs : Ludmilla Allard et Annaëlle Sorce
"""

import numpy as np
import matplotlib.pylab as plt
import probleme_a_2_corps as pb2
import os
import shutil


"""
Cas simple à 2 particules
"""

#nb d'objets :
N=pb2.N
#nb de coordonnées :
i=pb2.i
#masses :
m = pb2.m

#conditions initiales :
dt=0.01
T=2
X=pb2.X
V=pb2.V


# Création des tableaux contenants les positions et les vitesses
mvt_euler = pb2.mouvement_euler(X, V, i, N, dt, T)
mvt_lf = pb2.mouvement_lf(X, V, i, N, dt, T)

# Euler
X_euler = mvt_euler[0][0]   #extraction du tableau des x
Y_euler = mvt_euler[0][1]   #extraction du tableau des y

VX_euler = mvt_euler[1][0]
VY_euler = mvt_euler[1][1]

# Leapfrog
X_lf = mvt_lf[0][0]
Y_lf = mvt_lf[0][1]

VX_lf = mvt_lf[1][0]
VY_lf = mvt_lf[1][1]

plt.style.use('dark_background')

"""
Etude de la conservation de l'énergie
"""

def energie(X, Y, VX, VY):
    E = np.zeros(X.shape[1])
    for p1 in range(N) :
        E += m[p1] * (VX[p1, :]**2 + VY[p1, :]**2) /2
        for p2 in range(p1) :
            E -= m[p1]*m[p2] / np.sqrt((X[p2, :]-X[p1, :])**2 + (Y[p2, :]-Y[p1, :])**2)
    return(E)

energie_euler = energie(X_euler, Y_euler, VX_euler, VY_euler)
energie_lf = energie(X_lf, Y_lf, VX_lf, VY_lf)


'''
Tracé comparatif des conservations d'énergie
'''

plt.plot(energie_euler, label = "énergie avec Euler")
plt.plot(energie_lf, label = "énergie avec Leapfrog")
plt.legend()
plt.title("Comparatif des énergies à 2 corps")
plt.savefig("Comparatif-énergies-2-corps.pdf")



# supprime les dossiers contenant les images s'ils existent déjà
try : 
    shutil.rmtree("Mvt-2-part_euler")
except : pass
try : 
    shutil.rmtree("Mvt-2-part_leapfrog")
except : pass

# Creation des dossiers contenant les images
os.mkdir("Mvt-2-part_euler")
os.mkdir("Mvt-2-part_leapfrog")

"""
Boucle pour afficher les graphiques à chaque temps
"""


cpt = 0 # décompte pour les numéros des graphiques

#Pour Euler
for t in range(1, int(T/dt)+1, 2) :
    cpt += 1
    x = X_euler[:,t-1:t]
    y = Y_euler[:,t-1:t]
    
    colors = np.array((5,4))
    
    fig, ax = plt.subplots()
    
    ax.scatter(x,y, c = colors)
    ax.set(xlim=(-5, 5), xticks=np.arange(-5, 5),ylim=(-5,5), yticks=np.arange(-5,5))
    
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title("Position des deux particules avec la méthode d'Euler")
    plt.savefig('Mvt-2-part_euler/mvt_2_particules_%03g.png'%cpt)


cpt = 0
#Pour Leapfrog
for t in range(1, int(T/dt)+1, 2) :
    cpt += 1
    x = X_lf[:,t-1:t]
    y = Y_lf[:,t-1:t]
    
    colors = np.array((5,4))
    
    fig, ax = plt.subplots()
    
    ax.scatter(x,y, c = colors)
    ax.set(xlim=(-5, 5), xticks=np.arange(-5, 5),ylim=(-5,5), yticks=np.arange(-5,5))
    
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title("Position des deux particules avec la méthode Leapfrog")
    plt.savefig('Mvt-2-part_leapfrog/mvt_2_particules_%03g.png'%cpt)


# creation des vidéos
os.system("ffmpeg -y -r 10 -i Mvt-2-part_euler/mvt_2_particules_%03d.png mvt-2-part_euler.mp4")
shutil.rmtree("Mvt-2-part_euler")


os.system("ffmpeg -y -r 10 -i Mvt-2-part_leapfrog/mvt_2_particules_%03d.png mvt-2-part_leapfrog.mp4")
shutil.rmtree("Mvt-2-part_leapfrog")
