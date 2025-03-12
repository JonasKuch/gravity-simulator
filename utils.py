import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.constants import G


def newton_force(r, m1, m2):
    return G*(m1*m2)/(r**2)


def total_F(coords:list, masses:list) -> tuple:
    
    n = len(coords)

    alist = []
    Fsum = {(i+1) : np.zeros_like(coords[0], dtype=float) for i in range(len(coords))}

    for i, coord in enumerate(coords):
        for j in range(i+1, len(coords)):
            r = np.linalg.norm(coord - coords[j])
            if r == 0:
                continue
            unit = (coords[j] - coord) / r

            F1 = newton_force(r, masses[i], masses[j])*unit
            Fsum[i+1] += F1
            Fsum[j+1] -= F1

    for i in range(len(coords)):
        a = Fsum[i+1]/masses[i]
        alist.append(a)
    
    return list(Fsum.values()), alist


def leapfrog_integration(coords:list, velocities:list, masses:list, dt) -> tuple:
    
    n = len(coords)

    forces, accelerations = total_F(coords, masses)

    v_inter = []
    v_new = []
    coords_new = []

    for i in range(n):
        v_inter.append(velocities[i] + 0.5 * accelerations[i]*dt)
        coords_new.append(coords[i] + v_inter[i] * dt)
    
    forces_new, accelerations_new = total_F(coords_new, masses)

    for i in range(n):
        v_new.append(v_inter[i] + 0.5 * accelerations_new[i] * dt)

    return coords_new, v_new, forces_new


class body:

    def __init__(self, mass, coords, velocity):
        self.mass = mass
        self.loc = coords
        self.v = velocity
        self.trace = [coords]
    
    def draw_location(self, ax = None, size = None, color = None):
        if ax == None:
            fig 


