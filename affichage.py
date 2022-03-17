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

#conditions initiales :
dt=0.005
T=2
X=np.zeros((i,N))
X[0,1]=1
#V[1,1]=1
V=np.zeros((i,N))
V[1,1]=1

# Création des tableaux contenants les positions
mvt_euler = pb2.mouvement_euler(X, V, i, N, dt, T)
mvt_lf = pb2.mouvement_lf(X, V, i, N, dt, T)

tab_X_euler = mvt_euler[0][0]   #extraction du tableau des x
tab_Y_euler = mvt_euler[0][1]   #extraction du tableau des y

tab_X_lf = mvt_lf[0][0]
tab_Y_lf = mvt_lf[0][1]

plt.style.use('dark_background')
os.mkdir("Mvt-2-part_euler")
os.mkdir("Mvt-2-part_leapfrog")

'''
Boucle pour afficher les graphiques à chaque temps
'''

#Pour Euler
for t in range(1, int(T/dt)+1, 2) :
    
    x = tab_X_euler[:,t-1:t]
    y = tab_Y_euler[:,t-1:t]
    
    colors = np.array((5,4))
    
    fig, ax = plt.subplots()
    
    ax.scatter(x,y, c = colors)
    ax.set(xlim=(-5, 5), xticks=np.arange(-5, 5),ylim=(-5,5), yticks=np.arange(-5,5))
    
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title("Position des deux particules avec la méthode d'Euler")
    plt.savefig('Mvt-2-part_euler/mvt_2_particules_%03g.png'%t)


#Pour Leapfrog
for t in range(1, int(T/dt)+1, 2) :
    
    x = tab_X_lf[:,t-1:t]
    y = tab_Y_lf[:,t-1:t]
    
    colors = np.array((5,4))
    
    fig, ax = plt.subplots()
    
    ax.scatter(x,y, c = colors)
    ax.set(xlim=(-5, 5), xticks=np.arange(-5, 5),ylim=(-5,5), yticks=np.arange(-5,5))
    
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title("Position des deux particules avec la méthode Leapfrog")
    plt.savefig('Mvt-2-part_leapfrog/mvt_2_particules_%03g.png'%t)


# creation des vidéos
os.system("ffmpeg -y -r 10 -i Mvt-2-part_euler/mvt_2_particules_%03d.png mvt-2-part_euler.mp4")
#shutil.rmtree("Mvt-2-part_euler")


os.system("ffmpeg -y -r 10 -i Mvt-2-part_leapfrog/mvt_2_particules_%03d.png mvt-2-part_leapfrog.mp4")
#shutil.rmtree("Mvt-2-part_leapfrog")