import pandas as pd
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
from statsmodels.stats.weightstats import ztest
from statsmodels.stats.weightstats import DescrStatsW

'''
A empresa Suco Bom produz sucos de frutas em embalagens de 500 ml. Seu processo de produção é quase 
todo automatizado e as embalagens de sucos são preenchidas por uma máquina que às vezes apresenta um certo desajuste, 
levando a erros no preenchimento das embalagens para mais ou menos conteúdo. Quando o volume médio cai abaixo de 500 ml, 
a empresa se preocupa em perder vendas e ter problemas com os orgãos fiscalizadores. Quando o volume passa de 500 ml, 
a empresa começa a se preocupar com prejuízos no processo de produção.

O setor de controle de qualidade da empresa Suco Bom extrai, periodicamente, amostras de 50 embalagens para monitorar 
o processo de produção. Para cada amostra, é realizado um teste de hipóteses para avaliar se o maquinário se desajustou.
A equipe de controle de qualidade assume um nível de significância de 5%.

Suponha agora que uma amostra de 50 embalagens foi selecionada e que a média amostral observada foi de 503,24 ml. 
Esse valor de média amostral é suficientemente maior que 500 ml para nos fazer rejeitar a hipótese de que a média 
do processo é de 500 ml ao nível de significância de 5%?
'''

sample = [509, 505, 495, 510, 496, 509, 497, 502, 503, 505, 
           501, 505, 510, 505, 504, 497, 506, 506, 508, 505, 
           497, 504, 500, 498, 506, 496, 508, 497, 503, 501, 
           503, 506, 499, 498, 509, 507, 503, 499, 509, 495, 
           502, 505, 504, 509, 508, 501, 505, 497, 508, 507]

sample = pd.DataFrame(sample, columns=['Sample'])
sample.head()

sample_mean = sample.mean()[0]
desv_pad_sample = sample.std()[0]

mean = 500
alfa = 0.05
confidenc = 1 - alfa
n = 50

#H0 mean = 500
#H1 mean != 500
probability = 0.5 + confidenc / 2
z_alpha_2 = norm.ppf(probability)
z_alpha_1 = - z_alpha_2

z = (sample_mean - mean) / (desv_pad_sample / (np.sqrt(n)))
p_value = 2 * (1 - norm.cdf(z))

z, p_valor = ztest(x1=sample, value=mean)


if(z <= z_alpha_1 or z >= z_alpha_2):
    print('Reject H0')
else:
    print('Accept H0')

if(p_value <= alfa):
    print('Reject H0')
else:
    print('Accept H0')

'''
Um fabricante de farinha afirma que a quantidade média de farinha nas embalagens de seu principal produto é de 500 g. 
Um teste de pesagem em 30 embalagens amostradas ao acaso mostrou um peso médio igual à 485 g. 
Estudos anteriores afirmam que a distribuição dos pesos segue uma distribuição normal e que o desvio padrão populacional 
é igual a 20 g. Considerando um nível de significância igual a 5%, responda as seguintes questões:

1) Qual a hipótese nula a ser testada?
2) Qual o valor da estatística de teste?
3) Qual a conclusão do teste?
'''

mean_sample = 485
desv_pad = 20
mean = 500
alfa = 0.05
confidenc = 1 - alfa
n = 30

#H0 mean = 500
#H1 mean != 500
probability = (0.5 + (confidenc / 2))
z_alpha_2 = norm.ppf(probability)
z_alpha_1 = - z_alpha_2

z = (mean_sample - mean) / (desv_pad / np.sqrt(n))

print('z =', round(z, 4))
if(z <= z_alpha_1 or z >= z_alpha_2):
    print('Reject H0')
else:
    print('Accept H0')