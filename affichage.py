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


"""
Cas simple à 2 particules
"""

#nb d'objets :
N=pb2.N
#nb de coordonnées :
i=pb2.i

#conditions initiales :
dt=1
T=5
X=np.zeros((i,N))
X[0,1]=1
V=np.zeros((i,N))
V[0,1]=1
N=2
i=3

# Création des tableaux contenants les positions
mvt = pb2.mouvement(X,V,i,N,dt,T)

tab_X = mvt[0][0]   #extraction du tableau des x
tab_Y = mvt[0][1]   #extraction du tableau des y


plt.style.use('dark_background')

# Boucle pour afficher les graphiques à chaque temps
for t in range(1,T+1) :
    x = tab_X[:,t-1:t]
    y = tab_Y[:,t-1:t]
    print(x,"\n",y)
    
    colors = np.array((5,4))
    fig, ax = plt.subplots()
    
    ax.scatter(x,y, c = colors)
    ax.set(xlim=(-2, 8), xticks=np.arange(-2, 8))
    
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title("Position des deux particules")
    
    plt.show()