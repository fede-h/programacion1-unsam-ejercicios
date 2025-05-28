import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_parques = pd.read_csv('../Data/arbolado-en-espacios-verdes.csv')
df_veredas = pd.read_csv('../Data/arbolado-publico-lineal-2017-2018.csv')

df_tipas_parques = df_parques[df_parques['nombre_cie'] == 'Tipuana Tipu'].copy()
df_tipas_veredas = df_veredas[df_veredas['nombre_cientifico'] == 'Tipuana tipu'].copy()

df_tipas_parques = df_tipas_parques[['altura_tot', 'diametro']]
df_tipas_parques = df_tipas_parques.rename(columns ={
    'altura_tot' : 'altura'
})

df_tipas_veredas = df_tipas_veredas[['altura_arbol', 'diametro_altura_pecho']]
df_tipas_veredas = df_tipas_veredas.rename(columns={
    'altura_arbol' : 'altura',
    'diametro_altura_pecho' : 'diametro'
})

ambiente_parque = ['parque' for i in range(df_tipas_parques.shape[0])]
df_tipas_parques['ambiente'] = ambiente_parque

ambiente_vereda = ['vereda' for i in range(df_tipas_veredas.shape[0])]
df_tipas_veredas['ambiente'] = ambiente_vereda

df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques])

df_tipas.boxplot('diametro', by = 'ambiente')

df_tipas.boxplot('altura', by = 'ambiente')
