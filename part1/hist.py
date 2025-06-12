import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('../data/SpeedDatingData.csv',  encoding='latin1')
"""
for column in data.columns:
    print(column)
    plt.hist(data[column], bins = 20)
    plt.title("Rozkład atrybutu: " + column)
    plt.xlabel(column)
    plt.ylabel("Liczba wystąpień")
    plt.savefig("plots/hist/"+column + "_hist.png")
    plt.show()
   """
"""
qualities = ['attr', 'sinc', 'intel', 'fun', 'amb']
vals = ['1_1', '5_1', '7_2']
for quality in qualities:
    for val in vals:
        column = quality + val
        plt.hist(data[column], bins = 10)
        plt.title("Rozkład atrybutu: " + column)
        plt.xlabel(column)
        plt.ylabel("Liczba wystąpień")
        plt.savefig("plots/hist/"+column + "_hist.png")
        plt.show()
"""

for column in data.columns:
    print(column)
"""
string_columns = data.select_dtypes(include=['object', 'string']).columns
print(string_columns)
"""
