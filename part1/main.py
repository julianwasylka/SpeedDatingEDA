import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('../data/SpeedDatingData.csv',  encoding='latin1')
print(data['dec'])
print(data['match'])

data = data[['like','fun','shar']]
