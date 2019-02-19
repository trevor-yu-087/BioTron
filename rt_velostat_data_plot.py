import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

#create figure and data structure for plotting
fig = plt.figure()
ax = fig.add_subplot(1,1,1)

def updateGraph(i):
    with open("sensor_data.txt", "r") as file:
        graphData = file.read()
    lines = graphData.split('\n')
    if len(lines) > 3000:
        with open("sensor_data.txt", "w") as file:
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
    colors = data_point / 255
    ax.scatter(xs, ys, c=colors, cmap=plt.cm.get_cmap('inferno'))

    # format plot
    plt.title('Velostat Pressure Sensor')
    fig.colorbar(plt)
    ax.set_xticks((0., 1.))
    ax.set_yticks((0, 1, 2, 3, 4, 5))


ani = animation.FuncAnimation(fig, updateGraph, interval=100)
ax.set_ylim(-1, 7)
ax.set_xlim(-1, 2)
plt.show()