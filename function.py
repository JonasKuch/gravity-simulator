import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import G

def newton_force(r, m1, m2):
    return G*(m1*m2)/(r**2)


def F(coords, masses):
    
    n = len(coords)

    alist = []
    Fsum = {(i+1) : np.zeros_like(coords[0], dtype=float) for i in range(len(coords))}

    for i, coord in enumerate(coords):
        for j in range(i+1, len(coords)):
            r = np.linalg.norm(coord - coords[j])
            unit = (coords[j] - coord) / r

            F1 = newton_force(r, masses[i], masses[j])*unit
            Fsum[i+1] += F1
            Fsum[j+1] -= F1

    for i in range(len(coords)):
        a = Fsum[i+1]/masses[i]
        alist.append(a)
    
    return Fsum, alist


coords = [np.array([1, 1, 1]), np.array([1, 1, 2]), np.array([-1, 1, 1]), np.array([1, 0, 1]), np.array([1, 2, 1])]
masses = [1, 2, 3, 4, 5]

f, a = F(coords, masses)

coords_T = np.array(coords).T
a_T = np.array(a).T

fig = plt.figure()
ax = fig.add_subplot(projection = '3d')
ax.set_xlim(-4, 4)
ax.set_ylim(-4, 4)
ax.set_zlim(-4, 4)
ax.quiver(coords_T[0], coords_T[1], coords_T[2], a_T[0], a_T[1], a_T[2], length = 0.5, normalize = 'True')
plt.show()