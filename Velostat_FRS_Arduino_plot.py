import serial
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

ser = serial.Serial('COM4', 9600)
pressures = []
number = ''
time = 0
while True:
    file = open('\sensor_data.csv', 'a')
    data = ''
    while data != b'\n':
        data = ser.readline(1)
        if data != b'\r':
            number = number + data.decode('utf-8')

    file.write(str(number))
    number = ''
    file.flush()
    file.close()

