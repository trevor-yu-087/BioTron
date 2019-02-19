import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.axes import Axes


def read_csv(csvfile):
    df = pd.read_csv(csvfile, low_memory=False)
    data = df.values
    print(data)
    sensor_data = []
    for i in range(12):
        sensor = np.asarray(data[:,i])
        print(sensor)
        sensor_data.append(sensor)
    #signal = data[:, 0]
    return sensor_data

def read_csv_12(csvfile):
    df = pd.read_csv(csvfile, low_memory=False)
    data = df.values
    return data


data_array = read_csv('sensor_data.csv')

def plot_fsr_matrix(data_array):
    fig,ax = plt.subplots(nrows=1,ncols=1,figsize=(0.5,3))
    fig = plt.figure(figsize=(1,6))
    ax = fig.add_subplot(1,1,1)

    for i in range(12):
        value = data_array[i]
        print(value)
        plt.plot(np.floor(i/6), (11-i)%6, c=(1,(255-value)/255, (255-value)/255), marker= 's', ms='30')
    plt.xlim(-0.5,1.5)
    plt.ylim(-1,6)
    ax.set_facecolor('k')
    plt.show()


data_array_12 = read_csv_12('sensor_data.csv')
plot_fsr_matrix(data_array_12[1])
