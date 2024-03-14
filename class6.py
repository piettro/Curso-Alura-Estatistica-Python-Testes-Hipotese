from scipy.stats import chi
import pandas as pd
import numpy as np
from scipy.stats import wilcoxon
from scipy.stats import mannwhitneyu
from scipy.stats import norm
from scipy.stats import t as t_student

'''
Um novo tratamento para acabar com o hábito de fumar está sendo empregado em um grupo de 35 pacientes voluntários. De cada paciente testado foram obtidas as informações de quantidades de cigarros consumidos por dia antes e depois do término do tratamento. Assumindo um nível de confiança de 95% é possível concluir que, depois da aplicação do novo tratamento, houve uma mudança no hábito de fumar do grupo de pacientes testado?

Empregado quando se deseja comparar duas amostras relacionadas, amostras emparelhadas. Pode ser aplicado quando se deseja testar a diferença de duas condições, isto é, quando um mesmo elemento é submetido a duas medidas.
'''

smoke = {
    'Before': [39, 25, 24, 50, 13, 52, 21, 29, 10, 22, 50, 15, 36, 39, 52, 48, 24, 15, 40, 41, 17, 12, 21, 49, 14, 55, 46, 22, 28, 23, 37, 17, 31, 49, 49],
    'After': [16, 8, 12, 0, 14, 16, 13, 12, 19, 17, 17, 2, 15, 10, 20, 13, 0, 4, 16, 18, 16, 16, 9, 9, 18, 4, 17, 0, 11, 14, 0, 19, 2, 9, 6]
}
alfa = 0.05
confidence = 1 - alfa
n = 35

smoke = pd.DataFrame(smoke)
smoke.head()

mean_before = smoke.Before.mean()
mean_after = smoke.After.mean()
probability = (0.5 + (confidence / 2))

z_alpha_2 = norm.ppf(probability)
z_alpha_2.round(2)

smoke['Dif'] = smoke.After - smoke.Before
smoke['|Dif|'] = smoke.Dif.abs()
smoke.sort_values(by = '|Dif|', inplace = True)
smoke['Posto'] = range(1, len(smoke) + 1)
posto = smoke[['|Dif|', 'Posto']].groupby(['|Dif|']).mean()
posto.reset_index(inplace = True)
smoke.drop(['Posto'], axis = 1, inplace = True)
smoke = smoke.merge(posto, left_on='|Dif|', right_on='|Dif|', how = 'left')
smoke['Posto (+)'] = smoke.apply(lambda x: x.Posto if x.Dif > 0 else 0, axis = 1)
smoke['Posto (-)'] = smoke.apply(lambda x: x.Posto if x.Dif < 0 else 0, axis = 1)
smoke.drop(['Posto'], axis = 1, inplace = True)


T = min(smoke['Posto (+)'].sum(), smoke['Posto (-)'].sum())
mu_T = (n * (n + 1)) / 4
sigma_T = np.sqrt((n * (n + 1) * ((2 * n) + 1)) / 24)
Z = (T - mu_T) / sigma_T

print(Z <= -z_alpha_2)
print(Z >= z_alpha_2)

T, p_value = wilcoxon(smoke.Before, smoke.After)
print(T)
print(p_value)

print(p_value <= alfa)

'''
Em nosso dataset temos os rendimento dos chefes de domicílio obtidos da 
Pesquisa Nacional por Amostra de Domicílios - PNAD no ano de 2015. 
Um problema bastante conhecido em nosso país diz respeito a desigualdade de renda, principalmente entre homens e mulheres.
Duas amostras aleatórias, uma de 6 homens e outra com 8 mulheres, foram selecionadas em nosso dataset. 
Com o objetivo de comprovar tal desigualdade teste a igualdade das médias entra estas duas amostras com um nível de significância de 5%.
'''

data = pd.read_csv('Data/dados.csv')
male = data.query('Sexo == 1 and Renda > 0').sample(n = 8, random_state = 101).Renda
man = data.query('Sexo == 0 and Renda > 0').sample(n = 6, random_state = 101).Renda
mean_sample_male = male.mean()
mean_sample_man = man.mean()
alfa = 0.05
confidance = 1 - alfa
n_1 = len(man)
n_2 = len(male)

degree_freedom = n_1 + n_2 - 2
t_alpha = t_student.ppf(alfa, degree_freedom)
t_alpha.round(2)

H = pd.DataFrame(man)
H['Sexo'] = 'Homens'
M = pd.DataFrame(male)
M['Sexo'] = 'Mulheres'
sex = H.append(M)
sex.reset_index(inplace = True, drop = True)
sex.sort_values(by = 'Renda', inplace = True)
sex['Posto'] = range(1, len(sex) + 1)
posto = sex[['Renda', 'Posto']].groupby(['Renda']).mean()
posto.reset_index(inplace = True)
sex.drop(['Posto'], axis = 1, inplace = True)
sexo = sex.merge(posto, left_on='Renda', right_on='Renda', how = 'left')

Temp = sexo[['Sexo', 'Posto']].groupby('Sexo').sum()
R_1 = Temp.loc['Homens'][0]
R_2 = Temp.loc['Mulheres'][0]

u_1 = n_1 * n_2 + ((n_1 * (n_1 + 1)) / (2)) - R_1
u_2 = n_1 * n_2 + ((n_2 * (n_2 + 1)) / (2)) - R_2
u = min(u_1, u_2)
mu_u = (n_1 * n_2) / 2
sigma_u = np.sqrt(n_1 * n_2 * (n_1 + n_2 + 1) / 12)
Z = (u - mu_u) / sigma_u
print(Z.round(2))
print(Z <= t_alpha)

u, p_valor = mannwhitneyu(male, man, alternative='less')
print(u)
print(p_valor)
print(p_valor <= alfa)
'''
Desconfiado da eficiência dos cursos e materiais de estudo online da Alura, 
um professor resolveu realizar um teste com um grupo de 14 alunos de sua classe. 
Para isto, ele submeteu estes alunos a duas etapas distintas e logo depois de cada etapa, aplicou uma avaliação. 
Na etapa inicial, foram oferecidas aulas normais, sem a utilização do material de apoio da Alura.
Na segunda etapa, foram também oferecidas aulas normais, mas com a utilização do material de apoio da Alura. 
As notas obtidas pelos alunos estão na tabela abaixo:
Assinale a alternativa que apresenta o resultado do teste, não paramétrico de Wilcoxon, 
aplicado pelo professor (estatística de teste T e decisão do teste). Considere um nível de significância de 10%.
'''

sem_Alura = pd.Series([ 7,  8, 6, 6, 10, 4, 2, 5,  9, 2, 4, 9, 1, 10])
com_Alura = pd.Series([10, 10, 9, 9,  9, 7, 5, 8, 10, 6, 3, 7, 4,  8])

significancia = 0.10

T, p_valor = wilcoxon(sem_Alura, com_Alura)
print('T =', T)

if(p_valor <= significancia):
    print('Rejeitar H0')
else:
    print('Aceitar H0')

'''
Um professor acredita que alunos que praticam exercícios físicos têm uma performance média escolar superior àquela obtida por alunos que não praticam. 
Para provar sua teoria, selecionou duas amostras aleatórias, uma com 9 alunos que não praticam exercícios físicos e outra com 10 alunos que cultivam o
hábito de se exercitar. A tabela abaixo mostra as notas dos alunos no último ano:
Teste a hipótese da média das notas dos alunos que praticam exercícios ser maior que a média das notas dos alunos que não praticam. 
Assinale a alternativa que apresenta o resultado do teste (estatística de teste u e decisão do teste). Considere um nível de significância de 10%.
'''

sem_Exercicios = pd.Series([7, 6, 7, 8, 6, 8, 6, 9, 5])
com_Exercicios = pd.Series([8, 7, 6, 6, 8, 6, 10, 6, 7, 8])

significancia = 0.10

u, p_valor = mannwhitneyu(com_Exercicios, sem_Exercicios, alternative='greater')

print('u =', u)

if(p_valor <= significancia):
    print('Rejeitar H0')
else:
    print('Aceitar H0')