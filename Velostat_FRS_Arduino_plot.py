import serial

ser = serial.Serial('COM4', 9600, timeout=1)
pressures = []
number = ''
time = 0
while ser.is_open:
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

