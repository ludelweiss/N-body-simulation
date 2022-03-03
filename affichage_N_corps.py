"""
Modélisation à l'aide d'une interface graphique du problème à N corps
Un graphique des positions est tracé pour chaque temps dt donné,
et les graphiques sont assemblés pour obtenir une vidéo du mouvement

Séance 5

Auteurs : Ludmilla Allard et Annaëlle Sorce
"""

import numpy as np
import matplolib.pylab as plt

"""
Création des données
"""

np.random.seed(3)   #permet de conserver les memes nombres aléatoires à chaque fois

# positions des points :
x = 4 + np.random.normal(0, 2, 24)
y = 4 + np.random.normal(0, 2, len(x))

# tailles et couleurs :
sizes = np.random.uniform(15, 80, len(x))
colors = np.random.uniform(15, 80, len(x))


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