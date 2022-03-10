"""
Modélisation à l'aide d'une interface graphique du problème à N corps
Un graphique des positions est tracé pour chaque temps dt donné,
et les graphiques sont assemblés pour obtenir une vidéo du mouvement

Séances 5, 6

Auteurs : Ludmilla Allard et Annaëlle Sorce
"""

import numpy as np
import matplolib.pylab as plt
import probleme_a_N_corps as pbN


#Conditions initiales :
T= 10

plt.style.use('dark_background')

# Boucle pour afficher les graphiques à chaque temps

""" Il faut redéfinir les positions et les couleurs avec les bonnes données

for t in range(1,T+1) :
    
    x = tab_X[:,t-1:t]
    y = tab_Y[:,t-1:t]
    
    colors = np.array((5,4))
    
    fig, ax = plt.subplots()
    
    ax.scatter(x,y, c = colors)
    ax.set(xlim=(-2, 8), xticks=np.arange(-2, 8))
    
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title("Position des N étoiles")
    plt.savefig('Mvt-N-part/mvt_N_particules_%03g.png'%t)
"""