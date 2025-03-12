import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.constants import G
from utils import leapfrog_integration
from systems import system

coords, velocities, masses, names, colors, sizes, autoscale, axes_scales, dt = system('Sonnensystem')

traces_list = [[i] for i in coords]

fig = plt.figure()
ax = fig.add_subplot(projection="3d")
ax.view_init(elev=0, azim=180)

if autoscale == False:
    ax.set_xlim(axes_scales[0])
    ax.set_ylim(axes_scales[1])
    ax.set_zlim(axes_scales[2])

_, _, _, forces = leapfrog_integration(coords, velocities, masses, dt)

scats = []
traces = []
quivers = []
for i, coord in enumerate(coords):
    scats.append(ax.scatter(coord[0], coord[1], coord[2], label=names[i], color=colors[i], s = sizes[i]))
    traces_data = np.array(traces_list[i]).T
    traces.append(ax.plot(traces_data[0], traces_data[1], traces_data[2], color=colors[i]))
    quivers.append(ax.quiver(coord[0], coord[1], coord[2], forces[i][0], forces[i][1], forces[i][2], normalize = True, length = 2e10, color = colors[i]))


def update(frame, masses:list, dt:float, autoscale):

    global coords, velocities, axes_scales

    coords, velocities, forces_new, _ = leapfrog_integration(coords, velocities, masses, dt)

    if autoscale == True:
        all_coords_list = []
        for trace in traces_list:
            for i in trace:
                all_coords_list.append(i)
        all_coords = np.array(all_coords_list)

        margin = 1e10
        min_vals = all_coords.min(axis=0) - margin
        max_vals = all_coords.max(axis=0) + margin
        axes_scales = [(min_vals[0], max_vals[0]), (min_vals[1], max_vals[1]), (min_vals[2], max_vals[2])]

        ax.set_xlim(axes_scales[0])
        ax.set_ylim(axes_scales[1])
        ax.set_zlim(axes_scales[2])
    
    for i, coord in enumerate(coords):
        scats[i]._offsets3d = ([coord[0]], [coord[1]], [coord[2]])
        traces_list[i].append(coord)
        traces_data = np.array(traces_list[i]).T
        traces[i][0].set_data(traces_data[0], traces_data[1])
        traces[i][0].set_3d_properties(traces_data[2])
        quivers[i].remove()
        quivers[i] = ax.quiver(coord[0], coord[1], coord[2], forces_new[i][0], forces_new[i][1], forces_new[i][2], normalize = True, length = 2e10, color = colors[i])

    return scats, traces

ani= animation.FuncAnimation(fig=fig, func=update, frames=1000, interval=0, fargs=(masses, dt, autoscale), cache_frame_data=True)
plt.legend()
plt.show()