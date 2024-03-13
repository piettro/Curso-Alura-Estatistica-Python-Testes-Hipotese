import pandas as pd
import numpy as np
from scipy.stats import normaltest
import matplotlib.pyplot as plt

data = pd.read_csv('Data/dados.csv')
print(data.head())

alfa = 0.05

data['Renda'].hist(bins = 50)
plt.show()

stat_test, p_valor = normaltest(data['Renda'])
print(stat_test)
print(p_valor)
print(p_valor <= alfa)

data['Altura'].hist(bins = 50)
plt.show()

stat_test, p_valor = normaltest(data['Altura'])
print(stat_test)
print(p_valor)
print(p_valor <= alfa)