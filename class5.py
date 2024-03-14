from scipy.stats import chi
import pandas as pd
import numpy as np
from scipy.stats import chisquare
'''
Antes de cada partida do campeonato nacional de futebol, 
as moedas utilizadas pelos árbitros devem ser verificadas para se ter certeza de que não são viciadas, 
ou seja, que não tendam para determinado resultado. Para isso um teste simples deve ser realizado antes de cada partida. 
Este teste consiste em lançar a moeda do jogo 50 vezes e contar as frequências de CARAS e COROAS obtidas. 
A tabela abaixo mostra o resultado obtido no experimento:

A um nível de significância de 5%, é possível afirmar que a moeda não é honesta, 
isto é, que a moeda apresenta uma probabilidade maior de cair com a face CARA voltada para cima?
'''

F_observed = [17, 33]
F_expected = [25, 25]
alfa = 0.05
confidenc = 1 - alfa
k = 2 # Número de eventos possíveis
degree_freedom = k - 1

chi_2_alpha = chi.ppf(confidenc, degree_freedom) ** 2
print(chi_2_alpha)

chi_2 = ( (F_observed[0] - F_expected[0]) ** 2 /  F_expected[0] ) + ( (F_observed[1] - F_expected[1]) ** 2 /  F_expected[1] )
print(chi_2)

chi_2 = 0
for i in range(k):
  chi_2 += (F_observed[i] - F_expected[i]) ** 2 /  F_expected[i]
  
print(chi_2)

print(chi_2 > chi_2_alpha)

sqrt_chi_2 = np.sqrt(chi_2)
print(sqrt_chi_2)

p_value = chi.sf(sqrt_chi_2, df=1)
print(p_value)

chi_2, p_value = chisquare(f_obs=F_observed, f_exp=F_expected)
print(chi_2)
print(p_value)

print(p_value <= alfa)