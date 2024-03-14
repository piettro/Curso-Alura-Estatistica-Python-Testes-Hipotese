import pandas as pd
import numpy as np
from scipy.stats import t as t_student
from scipy.stats import norm
import matplotlib.pyplot as plt
from statsmodels.stats.weightstats import DescrStatsW, CompareMeans

'''
Em nosso dataset temos os rendimento dos chefes de domicílio obtidos da 
Pesquisa Nacional por Amostra de Domicílios - PNAD no ano de 2015. 
Um problema bastante conhecido em nosso país diz respeito a desigualdade de renda, 
principalmente entre homens e mulheres.
Duas amostras aleatórias, uma de 500 homens e outra com 500 mulheres, 
foram selecionadas em nosso dataset. Com o objetivo de comprovar tal desigualdade, 
teste a igualdade das médias entre estas duas amostras com um nível de significância de 1%.
'''
data = pd.read_csv('Data/dados.csv')

man = data.query('Sexo == 0').sample(n = 500, random_state = 101).Renda
male = data.query('Sexo == 1').sample(n = 500, random_state = 101).Renda

male_mean_sample = male.mean()
male_desvpad_sample = male.std()
man_mean_sample = man.mean()
man_desvpad_sample = man.std()

alfa = 0.01
confidence = 1 - alfa
n_male = 500
n_man = 500
D_0 = 0

probability = confidence
z_alpha = norm.ppf(probability)
print(z_alpha.round(2))

numerador = (man_mean_sample - male_mean_sample) - D_0
denominador = np.sqrt((man_desvpad_sample ** 2 / n_man) + (male_desvpad_sample ** 2 / n_male))
z = numerador / denominador
print(z)

print(z >= z_alpha)

test_man = DescrStatsW(man)
test_male = DescrStatsW(male)

test_A = test_man.get_compare(test_male)
z, p_valor = test_A.ztest_ind(alternative='larger', value=0)

test_B = CompareMeans(test_man, test_male)
z, p_valor = test_B.ztest_ind(alternative='larger', value=0)

print(p_valor <= alfa)

'''
Conclusão: Com um nível de confiança de 99% rejeitamos  H0 , isto é, 
concluímos que a média das rendas dos chefes de domicílios do sexo masculino 
é maior que a média das rendas das chefes de domicílios do sexo feminino. 
Confirmando a alegação de desigualdade de renda entre os sexos.
'''

'''
Um fabricante de cosméticos afirma que a adição de um novo composto químico em sua linha de shampoos 
consegue promover em mais de 2 centímetros o crescimento dos fios de cabelo em um período de 60 dias. 
Duas amostras de pessoas foram selecionadas e testadas, uma utilizando o shampoo novo (com o composto) 
e a outra com o shampoo antigo (sem o composto).

Os resultados (crescimento dos fios de cabelo em centímetros) podem ser verificados na Series abaixo:

shampoo_Novo = pd.Series([3.4, 4.9, 2.8, 5.5, 3.7, 2.5, 4.3, 4.6, 3.7, 3.4])
shampoo_Antigo = pd.Series([0.3, 1.2, 1.2, 1.7, 1.1, 0.6, 1.2, 1.5, 0.5, 0.7])

Assumindo um nível de confiança de 95% e considerando que as populações se distribuem como uma normal,
podemos acreditar na afirmação do fabricante do shampoo? Assinale a alternativa que apresenta a 
estatística de teste e a decisão correta do teste.

Um pouco mais de teoria: como se trata de um problema um pouco diferente do apresentado em nossa aula, 
vamos esclarecer alguns pontos para ajudar na solução:

1) Em testes entre duas amostras, quando realizamos a escolha da distribuição amostral adequada (passo 2) e perguntamos se n ≥ 30, 
temos que considerar que n = n1 + n2, onde n1 é o tamanho da primeira amostra e n2 o tamanho da segunda;

2) Quando n1 + n2 ≥ 30, utilizamos z (normal), e quando n1 + n2 < 30, 
σ não for conhecido e as populações forem normalmente distribuídas, utilizamos t (t-Student);

3) Quando utilizamos a tabela t de Student, em teste de duas amostras, 
os graus de liberdade são obtidos da seguinte forma: n1 + n2 - 2;

4) Quando o problema nos pergunta se podemos acreditar na afirmação do fabricante, 
está nos indicando o que devemos testar, ou seja, a nossa hipótese alternativa (H1), que no caso é:

Onde:

μ1 = Crescimento médio dos cabelos com o uso do novo shampoo
μ2 = Crescimento médio dos cabelos com o uso do shampoo antigo.
5) Em nosso próximo vídeo, utilizaremos o ztest_ind() para solucionar problemas como este. 
Um teste similar ao ztest_ind(), que utiliza a distribuição t de Student, é o ttest_ind(). 
Aqui, você será redirecionado para a documentação. 
Observe que o ttest_ind() retorna a estatística de teste, o p-valor e também os graus de liberdade.
'''


shampoo_new = pd.Series([3.4, 4.9, 2.8, 5.5, 3.7, 2.5, 4.3, 4.6, 3.7, 3.4])
shampoo_old = pd.Series([0.3, 1.2, 1.2, 1.7, 1.1, 0.6, 1.2, 1.5, 0.5, 0.7])

mean_a = shampoo_new.mean()
desvpad_a = shampoo_new.std()

mean_b = shampoo_old.mean()
desvpad_b = shampoo_old.std()

alfa = 0.05
confidence = 1 - alfa
n_A = len(shampoo_new)
n_B = len(shampoo_old)
D_0 = 2

degree_freedom = n_A + n_B - 2

t_alpha = t_student.ppf(confidence, degree_freedom)

numerador = (mean_a - mean_b) - D_0
denominador = np.sqrt((desvpad_a ** 2 / n_A) + (desvpad_b ** 2 / n_B))
t = numerador / denominador

print('t =', round(t, 4))

if(t >= t_alpha):
    print('Rejeitar H0')
else:
    print('Aceitar H0')