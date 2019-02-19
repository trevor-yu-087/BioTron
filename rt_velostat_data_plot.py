import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

#create figure and data structure for plotting
fig, ax = plt.subplots()


def updateGraph(i):
    with open("sensor_data.csv", "r") as file:
        graphData = file.read()
    lines = graphData.split('\n')
    if len(lines) > 3000:
        with open("sensor_data.csv", "w") as file:
            file.write('\n'.join(lines[len(lines) - 750:]) + '\n')

    # get data
    if len(lines) > 1:
        if len(lines[-1]) > 1:
            data_point = lines[-1].split(',')

    # plot data
    ax.clear()
    inds = np.linspace(0,11,num=12)
    xs = np.floor(inds / 6)
    ys = (11 - inds) % 6
    colors = inds / 255.
    im = ax.scatter(xs, ys, c=colors, cmap=plt.cm.get_cmap('inferno'), marker='s',s=1000, edgecolors='w')
    # legend = plt.legend()

    # format plot
    plt.title('Velostat Pressure Sensor')
    ax.set_xticks((0., 1.))
    ax.set_yticks((0, 1, 2, 3, 4, 5))
    ax.set_ylim(-1, 7)
    ax.set_xlim(-1, 2)
    # fig.colorbar(legend, ax=ax)



ani = animation.FuncAnimation(fig, updateGraph, interval=100)
ax.set_facecolor('k')
plt.show()