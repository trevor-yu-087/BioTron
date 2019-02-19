import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

fileName = 'Sample_foot_reading.csv'
df = pd.read_csv(fileName, low_memory=False)
#print(df)
data = df.values

# 50 samples / second
time = np.linspace(0,len(data)/50,len(data))
plt.plot(time,data)
plt.show()
