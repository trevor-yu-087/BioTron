import time
import numpy as np


def generate_data(t):
    return int(round(np.abs(127 + 127 * np.sin(np.pi*t/64))))


def generate_data_2(t):
    return int(round(np.abs(255/4*(np.sin(t/2)*((np.exp(np.cos(12*t)))-3*np.cos(4*t))))))


def step_fn(y,t):
    ys = (23,39,42,56,36,36,39,38,39,37,37,36,36,32,28,25,28,28,27,27,27,29,29,26,76,233,251,251,251,251,252,252,252,252,252,252,252,252,252,251,251,251,250,249,249,249,248,248,247,247,245,242,238,245,242,248,228,234,238,241,243,244,244,244,243,231,77,22)
    # len(ys) = 68
    if t < 0 or t > len(ys)-1:
        return 0
    else:
        return ys[t] - y


def generate_data_3(t):
    sensor = []
    sensor.append(step_fn(-10, t - 8))
    sensor.append(step_fn(5, t - 7))
    sensor.append(step_fn(-7, t - 5))
    sensor.append(step_fn(-10, t - 4))
    sensor.append(step_fn(0, t - 2))
    sensor.append(step_fn(0, t + 0))
    sensor.append(sensor[0] - 5)
    sensor.append(sensor[1] - 3)
    sensor.append(sensor[2] + 3)
    sensor.append(sensor[3] + 4)
    sensor.append(sensor[4] - 4)
    sensor.append(sensor[5] - 5)

    sensor = np.asarray(sensor)
    sensor[np.where(sensor > 255)] = 255
    sensor[np.where(sensor < 0)] = 0

    return sensor


def data_string_2(t):
    time = t%100
    if time > 80:
        return '0,0,0,0,0,0,0,0,0,0,0,0\n'
    else:
        data = generate_data_3(time)
        s = ''
        for i in range(12):
            s = s + str(data[i]) + ','
        s = s[:-1]
        s += '\n'
        return s



def data_string(t):
    s = ''
    for i in range(12):
        s = s + str(generate_data_2(t+i*2)) + ','
    s = s[:-1]
    s += '\n'
    return s

print(data_string(0))
print(data_string(1))
print(data_string_2(0))
print(data_string_2(4))

time_ = 0

file = open('sensor_data.csv', 'a')
file.write('sensor1,sensor2,sensor3,sensor4,sensor5,sensor6,sensor7,sensor8,sensor9,sensor10,sensor11,sensor12'+'\n')
file.write(data_string_2(0))
file.flush()
file.close()



while True:
    file = open('sensor_data.csv', 'a')
    file.write(data_string_2(time_))
    file.flush()
    file.close()
    time_ += 1
    time.sleep(0.01)
