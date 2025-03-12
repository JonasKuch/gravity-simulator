import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.constants import G
from utils import leapfrog_integration


coords = [np.array([0, 0, 0], dtype=float), np.array([0, 1.5e11, 0], dtype=float), np.array([0, 1.5e11, 3.84e8], dtype=float)]
coords_T = np.array(coords).T

coords_list = [coords[-1]]
coords_list_T = np.array(coords[-1]).T

velocities = [np.array([0, 0, 0], dtype=float), np.array([0, 0, 30000], dtype=float), np.array([0, 1000, 30000], dtype=float)]
masses = [1.989e30, 5.972e24, 7.35e22]
dt = 10000


fig = plt.figure()
ax = fig.add_subplot(projection="3d")
ax.set(xlim3d=(-1.5e11, 1.5e11), xlabel='X')
ax.set(ylim3d=(-1.5e11, 1.5e11), ylabel='Y')
ax.set(zlim3d=(-1.5e11, 1.5e11), zlabel='Z')

scat = ax.scatter(coords_T[0], coords_T[1], coords_T[2])
trace = ax.plot(coords_list_T[0], coords_list_T[1], coords_list_T[2])

print(type(scat))


def update(frame, masses:list, dt:float):

    global coords, velocities

    coords, velocities, forces = leapfrog_integration(coords, velocities, masses, dt)
    coords_T = np.array(coords).T

    coords_list.append(coords[-1])
    coords_list_T = np.array(coords_list).T
    
    scat._offsets3d = (coords_T[0], coords_T[1], coords_T[2])
    trace[0].set_data(coords_list_T[0], coords_list_T[1])
    trace[0].set_3d_properties(coords_list_T[2])

    return scat, trace

ani= animation.FuncAnimation(fig=fig, func=update, frames=1000, interval=0, fargs=(masses, dt), cache_frame_data=True)
plt.show()