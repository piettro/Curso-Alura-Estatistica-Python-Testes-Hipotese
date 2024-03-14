import pandas as pd
import numpy as np
from scipy.stats import t as t_student
from scipy.stats import norm
import matplotlib.pyplot as plt
from statsmodels.stats.weightstats import DescrStatsW
'''
Um famoso fabricante de refrigerantes alega que uma lata de 350 ml de seu principal 
produto contém, no máximo, 37 gramas de açúcar. Esta alegação nos leva a entender que 
a quantidade média de açúcar em uma lata de refrigerante deve ser igual ou menor que 37 g.

Um consumidor desconfiado e com conhecimentos em inferência estatística resolve testar a 
alegação do fabricante e seleciona, aleatóriamente, em um conjunto de estabelecimentos distintos,
uma amostra de 25 latas do refrigerante em questão. 
Utilizando o equipamento correto o consumidor obteve as quantidades de açúcar em todas as 
25 latas de sua amostra.

Assumindo que essa população se distribua aproximadamente como uma normal e 
considerando um nível de significância de 5%, é possível aceitar como válida a 
alegação do fabricante?
'''

sample = [37.27, 36.42, 34.84, 34.60, 37.49, 
           36.53, 35.49, 36.90, 34.52, 37.30, 
           34.99, 36.55, 36.29, 36.06, 37.42, 
           34.47, 36.70, 35.86, 36.80, 36.92, 
           37.04, 36.39, 37.32, 36.64, 35.45]

sample = pd.DataFrame(sample, columns=['Amostra'])
print(sample.head())

mean_sample = sample.mean()[0]
desv_pad_sample = sample.std()[0]

mean = 37
alfa = 0.05
confidenc = 1 - alfa
n = 25
degrees_freedom = n - 1

t_alpha = t_student.ppf(confidenc, degrees_freedom)
t = (mean_sample - mean) / (desv_pad_sample / np.sqrt(n))
p_value = t_student.sf(t, df = 24)
print(f't: {t}')
print(f'p-value: {p_value}')

##
if(t >= t_alpha):
    print('Reject H0')
else:
    print('Accept H0')

if(p_value <= alfa):
    print('Reject H0')
else:
    print('Accept H0')

test = DescrStatsW(sample)
t, p_value, df = test.ttest_mean(value = mean, alternative = 'larger')
print(t[0])
print(p_value[0])
print(df)

if(p_value[0] <= alfa):
    print('Reject H0')
else:
    print('Accept H0')

'''
A empresa Limpa Esgoto garante ser capaz de realizar o tratamento de esgoto e obter, no máximo, 
150 g de impurezas para cada mil litros de esgoto tratado. Vinte amostras de mil litros de esgoto apresentaram, 
em média, 230 g de impurezas e desvio padrão amostral igual a 90 g.

Assumindo alfa igual a 5% e população normalmente distribuída, seria possível discordar da empresa Limpa Esgoto? 
'''
sample_mean = 230
desv_pad_sample = 90
mean = 150
alfa = 0.05
confidenc = 1 - alfa
n = 20
degrees_freedom = n - 1

t_alpha = t_student.ppf(confidenc, degrees_freedom)

t = (sample_mean - mean) / (desv_pad_sample / np.sqrt(n))

print('t(alpha) =', round(t_alpha, 4))
print('t =', round(t, 4))
if(t >= t_alpha):
    print('Reject H0')
else:
    print('Accept H0')


'''
A pizzaria Muito Queijo alega que a quantidade de queijo em suas pizzas tamanho família é de, no mínimo, 350 g.
Uma amostra de 35 pizzas tamanho família revelou uma média de 330 g de queijo por pizza. 
O desvio padrão amostral foi de 80 g.

Assumindo alfa igual a 5% e população normalmente distribuída, seria possível discordar da alegação da pizzaria? 
'''
sample_mean = 330
desv_pad_sample = 80
mean = 350
alfa = 0.05
confidenc = 1 - alfa
n = 35

z_alpha = norm.ppf(confidenc)

z = (sample_mean - mean) / (desv_pad_sample / np.sqrt(n))

print('z(alpha) =', round(z_alpha, 3))
print('z =', round(z, 3))
if(z <= -z_alpha):
    print('Reject H0')
else:
    print('Accept H0')