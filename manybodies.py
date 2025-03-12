import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.constants import G
from utils import leapfrog_integration


'''
Sonne, Erde, Mond
'''
# coords = [np.array([0, 0, 0], dtype=float), np.array([0, 1.5e11, 0], dtype=float), np.array([0, 1.5e11 + 3.84e8, 0], dtype=float)]
# velocities = [np.array([0, 0, 0], dtype=float), np.array([0, 0, 30000], dtype=float), np.array([0, 0, 1000 + 30000], dtype=float)]
# masses = [1.989e30, 5.972e24, 7.35e22]
# names = ['sun', 'earth', 'moon']
# colors = ['orange', 'cornflowerblue', 'grey']
# autoscale = False
# axes_scales = [(-2e11, 2e11), (-2e11, 2e11), (-2e11, 2e11)]
# dt = 1000

'''
Drei gleiche Massen
'''
coords = [np.array([1.5e11, 0, 0], dtype=float), np.array([0, 1.5e11, 0], dtype=float), np.array([0, 0, 1.5e11], dtype=float)]
velocities = [np.array([30000, 0, 0], dtype=float), np.array([0, 0, -30000], dtype=float), np.array([0, 30000, 0], dtype=float)]
masses = [1.989e30, 1.989e30, 1.989e30]
names = ['mass1', 'mass2', 'mass3']
colors = ['red', 'blue', 'green']
autoscale = True
axes_scales = None
dt = 10000

'''
Sonnensystem
'''
# coords = [np.array([0, 0, 0], dtype=float), np.array([0, 1.5e11, 0], dtype=float)]
# velocities = [np.array([0, 0, 0], dtype=float), np.array([0, 0, 30000], dtype=float)]
# masses = [1.989e30, 5.972e24]
# colors = ['orange', 'cornflowerblue', 'grey']
# autoscale = False
# axes_scales = [(-2e11, 2e11), (-2e11, 2e11), (-2e11, 2e11)]
# dt = 1000 ----> alles noch nicht ready


traces_list = [[i] for i in coords]

fig = plt.figure()
ax = fig.add_subplot(projection="3d")

if autoscale == False:
    ax.set_xlim(axes_scales[0])
    ax.set_ylim(axes_scales[1])
    ax.set_zlim(axes_scales[2])

scats = []
traces = []
forces = []
for i, coord in enumerate(coords):
    scats.append(ax.scatter(coord[0], coord[1], coord[2], label=names[i], color=colors[i]))
    traces_data = np.array(traces_list[i]).T
    traces.append(ax.plot(traces_data[0], traces_data[1], traces_data[2], color=colors[i]))


def update(frame, masses:list, dt:float, autoscale):

    global coords, velocities

    coords, velocities, forces = leapfrog_integration(coords, velocities, masses, dt)
    coords_T = np.array(coords).T
    
    for i, coord in enumerate(coords):
        scats[i]._offsets3d = ([coord[0]], [coord[1]], [coord[2]])
        traces_list[i].append(coord)
        traces_data = np.array(traces_list[i]).T
        traces[i][0].set_data(traces_data[0], traces_data[1])
        traces[i][0].set_3d_properties(traces_data[2])
    
    if autoscale == True:
        all_coords_list = []
        for trace in traces_list:
            for i in trace:
                all_coords_list.append(i)
        all_coords = np.array(all_coords_list)

        margin = 1e10
        min_vals = all_coords.min(axis=0) - margin
        max_vals = all_coords.max(axis=0) + margin

        ax.set_xlim(min_vals[0], max_vals[0])
        ax.set_ylim(min_vals[1], max_vals[1])
        ax.set_zlim(min_vals[2], max_vals[2])

    return scats, traces

ani= animation.FuncAnimation(fig=fig, func=update, frames=1000, interval=0, fargs=(masses, dt, autoscale), cache_frame_data=True)
plt.legend()
plt.show()