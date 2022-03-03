"""
Création des données initiales et modélisation à l'aide d'une interface graphique
On trace un graphique  pour chaque temps dt donné

auteurs : Ludmilla Allard et Annaëlle Sorce
"""

import numpy as np
import matplotlib.pylab as plt
import probleme_a_2_corps as pb2


plt.style.use('dark_background')

"""
Création des données
"""
'''
np.random.seed(3)   #permet de conserver les memes nombres aléatoires à chaque fois

# positions des points :
x = 4 + np.random.normal(0, 2, 24)
y = 4 + np.random.normal(0, 2, len(x))

# tailles et couleurs :
sizes = np.random.uniform(15, 80, len(x))
colors = np.random.uniform(15, 80, len(x))
'''

"""
Cas simple à 2 particules
"""
# Variables
G=1
ma=1
mb=1

#nb d'objets :
N=2
#nb de coordonnées :
i=3


#conditions initiales :
dt=1
T=4
X=np.zeros((i,N))
X[0,1]=1
V=np.zeros((i,N))
V[0,1]=1
N=2
i=3

mvt = pb2.mouvement(X,V,i,N,dt,T)



tab_X = mvt[0][0]   #extraction du tableau des x
tab_Y = mvt[0][1]   #extraction du tableau des y
print(tab_Y)


"""
Tracé du graphique

fig, ax = plt.subplots()

#ax.scatter(x, y, s=sizes, c=colors, vmin=0, vmax=100)

ax.scatter(x, y, vmin=0, vmax=100)

ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Positions des étoiles")

plt.show()
"""


# Boucle pour afficher les graphiques à chaque temps
for t in range(1,T+1) :
    x = tab_X[:,t-1:t]
    y = tab_Y[:,t-1:t]
    print(x,"\n",y)
    
    fig, ax = plt.subplots()
    
    ax.scatter(x,y)
    ax.set(xlim=(-2, 8), xticks=np.arange(-2, 8))
    
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title("Position des deux particules")
    
    plt.show()
