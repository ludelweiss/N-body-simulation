import numpy as np
import matplotlib.pylab as plt
import probleme_a_2_corps as pb2

"""
Interface graphique
"""

plt.plot(pb2.tab_euler_X, pb2.tab_euler_V, label = "Trajectoire des particules")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()