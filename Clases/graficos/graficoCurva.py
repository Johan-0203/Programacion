import pandas as pd
ecgData = pd.read_csv('ecg.csv',encoding='UTF-8',header=0,delimiter=';').to_dict()
print(ecgData.keys())