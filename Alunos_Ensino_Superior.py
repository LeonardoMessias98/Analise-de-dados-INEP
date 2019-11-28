#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


df_dados2014 = pd.read_csv ('DM_ALUNO2014.CSV', delimiter = '|', encoding = 'iso-8859-1', usecols = ['CO_TIPO_ESCOLA_ENS_MEDIO'])
df_dados2015 = pd.read_csv ('DM_ALUNO2015.CSV', delimiter = '|', encoding = 'iso-8859-1', usecols = ['CO_TIPO_ESCOLA_ENS_MEDIO'])
df_dados2016 = pd.read_csv ('DM_ALUNO2016.CSV', delimiter = '|', encoding = 'iso-8859-1', usecols = ['CO_TIPO_ESCOLA_ENS_MEDIO'])
df_dados2017 = pd.read_csv ('DM_ALUNO2017.CSV', delimiter = '|', encoding = 'iso-8859-1', usecols = ['TP_ESCOLA_CONCLUSAO_ENS_MEDIO'])
df_dados2018 = pd.read_csv ('DM_ALUNO2018.CSV', delimiter = '|', encoding = 'iso-8859-1', usecols = ['TP_ESCOLA_CONCLUSAO_ENS_MEDIO'])


# In[3]:


PUB2014 = (df_dados2014.query('CO_TIPO_ESCOLA_ENS_MEDIO == 1')['CO_TIPO_ESCOLA_ENS_MEDIO'].count())
PUB2015 = (df_dados2015.query('CO_TIPO_ESCOLA_ENS_MEDIO == 1')['CO_TIPO_ESCOLA_ENS_MEDIO'].count())
PUB2016 = (df_dados2016.query('CO_TIPO_ESCOLA_ENS_MEDIO == 1')['CO_TIPO_ESCOLA_ENS_MEDIO'].count())
PUB2017 = (df_dados2017.query('TP_ESCOLA_CONCLUSAO_ENS_MEDIO == 2')['TP_ESCOLA_CONCLUSAO_ENS_MEDIO'].count())
PUB2018 = (df_dados2018.query('TP_ESCOLA_CONCLUSAO_ENS_MEDIO == 2')['TP_ESCOLA_CONCLUSAO_ENS_MEDIO'].count())


# In[4]:


PRIV2014 = (df_dados2014.query('CO_TIPO_ESCOLA_ENS_MEDIO == 0')['CO_TIPO_ESCOLA_ENS_MEDIO'].count())
PRIV2015 = (df_dados2015.query('CO_TIPO_ESCOLA_ENS_MEDIO == 0')['CO_TIPO_ESCOLA_ENS_MEDIO'].count())
PRIV2016 = (df_dados2016.query('CO_TIPO_ESCOLA_ENS_MEDIO == 0')['CO_TIPO_ESCOLA_ENS_MEDIO'].count())
PRIV2017 = (df_dados2017.query('TP_ESCOLA_CONCLUSAO_ENS_MEDIO == 1')['TP_ESCOLA_CONCLUSAO_ENS_MEDIO'].count())
PRIV2018 = (df_dados2018.query('TP_ESCOLA_CONCLUSAO_ENS_MEDIO == 1')['TP_ESCOLA_CONCLUSAO_ENS_MEDIO'].count())


# In[54]:


x1 = [2014.1, 2015.1, 2016.1, 2017.1, 2018.1]
x2 = [2014, 2015, 2016, 2017, 2018]
y1 = [(PUB2014),(PUB2015),(PUB2016),(PUB2017),(PUB2018)]
y2 = [(PRIV2014),(PRIV2015),(PRIV2016),(PRIV2017),(PRIV2018)]

plt.title('Alunos do Ensino Superior')
plt.xlabel('ANOS')
plt.ylabel('ALUNOS')
plt.bar(x1, y1, label ='Alunos quem vieram do Ensino Publico')
plt.bar(x2, y2, label ='Alunos que vieram do Ensino Privado')
plt.legend(bbox_to_anchor = (1.01, 1),loc='upper left', borderaxespad=0.)
plt.show()

print(f'Em 2014 \033[0;32m{PUB2014} alunos\033[m que ingressaram na faculdade vieram do \033[0;34mensino publico\033[m.\nE \033[0;32m{PRIV2014} alunos\033[m vieram do \033[0;31mensino privado\033[m.\n')
print(f'Em 2015 \033[0;32m{PUB2015} alunos\033[m que ingressaram na faculdade vieram do \033[0;34mensino publico\033[m.\nE \033[0;32m{PRIV2015} alunos\033[m vieram do \033[0;31mensino privado\033[m.\n')
print(f'Em 2016 \033[0;32m{PUB2016} alunos\033[m que ingressaram na faculdade vieram do \033[0;34mensino publico\033[m.\nE \033[0;32m{PRIV2016} alunos\033[m vieram do \033[0;31mensino privado\033[m.\n')
print(f'Em 2017 \033[0;32m{PUB2017} alunos\033[m que ingressaram na faculdade vieram do \033[0;34mensino publico\033[m.\nE \033[0;32m{PRIV2017} alunos\033[m vieram do \033[0;31mensino privado\033[m.\n')
print(f'Em 2018 \033[0;32m{PUB2018} alunos\033[m que ingressaram na faculdade vieram do \033[0;34mensino publico\033[m.\nE \033[0;32m{PRIV2018} alunos\033[m vieram do \033[0;31mensino privado\033[m.\n')


# In[ ]:




