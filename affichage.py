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
np.random.seed(3)   #permet de conserver les memes nombres aléatoires à chaque fois

# positions des points :
x = 4 + np.random.normal(0, 2, 24)
y = 4 + np.random.normal(0, 2, len(x))

# tailles et couleurs :
sizes = np.random.uniform(15, 80, len(x))
colors = np.random.uniform(15, 80, len(x)) #définir couleur en fonction des caractéristiques de l'étoile

# tracé de la figure
fig, ax = plt.subplots()

ax.scatter(x, y, s=sizes, c=colors, vmin=0, vmax=100)

ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Positions des particules")

plt.show()