import pandas as pd
import matplotlib.pyplot as plt
ppgData = pd.read_csv('ppg.csv',encoding='UTF-8',header=0,delimiter=';').to_dict()
muestras = list(ppgData['muestra'].values())
valores = list(ppgData['valor'].values())
plt.plot(muestras,valores)
plt.show()