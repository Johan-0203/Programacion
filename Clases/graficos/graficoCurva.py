import pandas as pd
import matplotlib.pyplot as plt
ecgData = pd.read_csv('ecg.csv',encoding='UTF-8',header=0,delimiter=';').to_dict()
muestras = list(ecgData['muestra'].values())
valores = list(ecgData['valor'].values())
plt.plot(muestras,valores)
plt.show()