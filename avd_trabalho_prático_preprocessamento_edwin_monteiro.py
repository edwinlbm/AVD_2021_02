# -*- coding: utf-8 -*-
"""AVD_Trabalho Prático_PreProcessamento_Edwin Monteiro.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NjTsKquRc53t-xZkvSkfFfEV4XL7Z3nJ

# Bibliotecas
"""

import pandas as pd
import numpy as np
import math

"""# Leitura do dataframe"""

df_mamo = pd.read_csv('https://raw.githubusercontent.com/edwinlbm/AVD_2021_02/main/mammographic_masses.data?token=AEEU35VOFESX3WSNC3HOLZLBJDMGM', delimiter = ',')

df_mamo.head(10)

"""### Ajuste no nome dos atributos"""

df_mamo_rotulada = pd.read_csv('https://raw.githubusercontent.com/edwinlbm/AVD_2021_02/main/mammographic_masses.data?token=AEEU35VOFESX3WSNC3HOLZLBJDMGM', delimiter = ',', names=['BI-RADS','Idade','Forma', 'Contorno', 'Densidade', 'Severidade'])

df_mamo_atual = df_mamo_rotulada.copy(deep=True)

"""### Rotulação dos dados"""

df_mamo_atual.head(10)

df_mamo_atual['Severidade'].replace({1: 'maligno', 0: 'benigno'}, inplace=True)

df_mamo_atual['Forma'].replace({'1': 'redonda', '2': 'oval', '3':'lobular', '4':'irregular'}, inplace=True)

df_mamo_atual['Contorno'].replace({'1': 'circunscrita', '2': 'microlobulada', '3':'obscura', '4':'mal definida', '5': 'especulada'}, inplace=True)

df_mamo_atual['Densidade'].replace({'1': 'alta', '2': 'iso', '3':'baixa', '4':'gordurosa'}, inplace=True)

df_mamo_atual.head(10)

# Dados ausentes em BI-RADS
df_mamo_atual[df_mamo_atual['BI-RADS'] == '?']

"""# Exercício 1.1. Atributo BI-RADS"""

df_exercicio_1_1 = df_mamo_atual.copy(deep=True)

def exercicio_1_1(df_exercicio_1_1):
    #seleção de dataframe contendo as informações de BI-RADS e Severidade: Maligno
    df_freq_bi_rads_maligno = df_exercicio_1_1[['BI-RADS', 'Severidade']]
    df_freq_bi_rads_maligno = df_freq_bi_rads_maligno.loc[(df_freq_bi_rads_maligno['Severidade'] == 'maligno')]

    # value_counts() ordena a frequência em ordem decrescente, logo basta acessar o índice 0 para obter o valor de maior frequência
    freq_bi_rads_maligno = df_freq_bi_rads_maligno['BI-RADS'].value_counts().keys().tolist()[0]

    #seleção de dataframe contendo as informações de BI-RADS e Severidade: Benigno
    df_freq_bi_rads_benigno = df_exercicio_1_1[['BI-RADS', 'Severidade']]
    df_freq_bi_rads_benigno = df_freq_bi_rads_benigno.loc[(df_freq_bi_rads_benigno['Severidade'] == 'benigno')]

    # value_counts() ordena a frequência em ordem decrescente, logo basta acessar o índice 0 para obter o valor de maior frequência
    freq_bi_rads_benigno = df_freq_bi_rads_benigno['BI-RADS'].value_counts().keys().tolist()[0]

    lista_index_birads_benigno = df_exercicio_1_1[(df_exercicio_1_1['BI-RADS'] == '?') & (df_exercicio_1_1['Severidade'] == 'benigno')].index
    # Dada a lista de linhas que ocorre o problema, substitui-se '?' pelo valor de maior frequência na coluna [BI-RADS] também acessível como coluna [0]
    df_exercicio_1_1.iloc[lista_index_birads_benigno, [0]] = freq_bi_rads_benigno

    lista_index_birads_maligno = df_exercicio_1_1[(df_exercicio_1_1['BI-RADS'] == '?') & (df_exercicio_1_1['Severidade'] == 'maligno')].index
    # Dada a lista de linhas que ocorre o problema, substitui-se '?' pelo valor de maior frequência na coluna [BI-RADS] também acessível como coluna [0]
    df_exercicio_1_1.iloc[lista_index_birads_maligno,[0]] = freq_bi_rads_maligno
    
exercicio_1_1(df_exercicio_1_1)

# Dados Ausentes - Dataset original
df_mamo_atual[(df_mamo_atual['BI-RADS'] == '?')]

# Dados Preenchidos no dataset df_exercicio_1_1

df_exercicio_1_1.loc[df_mamo_atual[(df_mamo_atual['BI-RADS'] == '?') & (df_mamo_atual['Severidade'] == 'maligno')].index]

df_exercicio_1_1.loc[df_mamo_atual[(df_mamo_atual['BI-RADS'] == '?') & (df_mamo_atual['Severidade'] == 'benigno')].index]

"""# Exercício 1.2. Atributo Idade

"""

df_exercicio_1_2 = df_exercicio_1_1.copy(deep=True)

df_exercicio_1_2[(df_exercicio_1_2['Idade'] == '?') & (df_exercicio_1_2['Severidade'] == 'maligno')]

df_media_maligno_ausente = df_exercicio_1_2[(df_exercicio_1_2['Idade'] == '?') & (df_exercicio_1_2['Severidade'] == 'maligno')]
df_media_maligno_ausente['Idade'].index

def exercicio_1_2(df_exercicio_1_2):
    classes_severidade = df_exercicio_1_2['Severidade'].unique()
    for nome in range(len(classes_severidade)):        
        if df_exercicio_1_2[(df_exercicio_1_2['Idade'] == '?') & (df_exercicio_1_2['Severidade'] == classes_severidade[nome])]['Idade'].count() > 0:
            df_media = df_exercicio_1_2[(df_exercicio_1_2['Idade'] != '?') & (df_exercicio_1_2['Severidade'] == classes_severidade[nome])]
            lista_idade = []
            for i in df_media['Idade']:
                lista_idade.append(float(i))
            lista_idade = np.array(lista_idade)
            media_idade = lista_idade.sum() / len(lista_idade)

            media_idade = math.floor(media_idade)
            media_idade
            #print("media " + classes_severidade[nome], media_idade)
            df_linha_ausente = df_exercicio_1_2[(df_exercicio_1_2['Idade'] == '?') & (df_exercicio_1_2['Severidade'] == classes_severidade[nome])]
            #print(df_linha_ausente)
            lista_linha_ausente = df_linha_ausente['Idade'].index
            #print(df_linha_ausente['Idade'])
            df_exercicio_1_2.iloc[lista_linha_ausente, [1]] = media_idade

exercicio_1_2(df_exercicio_1_2)

df_exercicio_1_2

#df_exercicio_1_2.iloc[[6],[1]]

"""# Exercício 1.3. Atributo Forma"""

df_exercicio_1_3 = df_exercicio_1_2.copy(deep=True)

def exercicio_1_3(df_exercicio_1_3):
    nome_classe_severidade = df_exercicio_1_3['Severidade'].unique()
    for nome_classe in nome_classe_severidade: 
        df_linha_ausente = df_exercicio_1_3[(df_exercicio_1_3['Forma'] == '?') & (df_exercicio_1_3['Severidade'] == nome_classe)]
        if df_linha_ausente['Forma'].count() > 0:
            df_contagem = df_exercicio_1_3[(df_exercicio_1_3['Forma'] != '?') & (df_exercicio_1_3['Severidade'] == nome_classe)]
            frequencia_forma_valor = df_contagem['Forma'].value_counts().index.tolist()[0]
            #frequencia_forma_contagem = df_contagem['Forma'].value_counts()[0]
            df_exercicio_1_3.iloc[df_linha_ausente['Forma'].index, [2]] = frequencia_forma_valor 
            #= frequencia_forma_valor

exercicio_1_3(df_exercicio_1_3)

df_exercicio_1_3

"""# Exercício 1.4. Atributo Contorno"""

df_exercicio_1_4 = df_exercicio_1_3.copy(deep=True)

#idx_maligno = df_exercicio_1_4[(df_exercicio_1_4['Contorno'] == '?') & (df_exercicio_1_4['Severidade'] == 'maligno')]['Contorno'].index

#idx_benigno = df_exercicio_1_4[(df_exercicio_1_4['Contorno'] == '?') & (df_exercicio_1_4['Severidade'] == 'benigno')]['Contorno'].index

def exercicio_1_4(df_exercicio_1_4):
    nome_classe_contorno = df_exercicio_1_4['Severidade'].unique()
    for nome_classe in nome_classe_contorno: 
        df_linha_ausente = df_exercicio_1_4[(df_exercicio_1_4['Contorno'] == '?') & (df_exercicio_1_4['Severidade'] == nome_classe)]
        if df_linha_ausente['Contorno'].count() > 0:
            df_contagem = df_exercicio_1_4[(df_exercicio_1_4['Contorno'] != '?') & (df_exercicio_1_4['Severidade'] == nome_classe)]
            frequencia_contorno_valor = df_contagem['Contorno'].value_counts().index.tolist()[0]
            #frequencia_forma_contagem = df_contagem['Forma'].value_counts()[0]
            df_exercicio_1_4.iloc[df_linha_ausente['Contorno'].index, [3]] = frequencia_contorno_valor 
            #= frequencia_forma_valor

exercicio_1_4(df_exercicio_1_4)

df_exercicio_1_4

#df_exercicio_1_4.iloc[idx_maligno,[3]]

#df_exercicio_1_4.iloc[idx_benigno,[3]]

"""# Exercício 1.5. Atributo Densidade"""

df_exercicio_1_5 = df_exercicio_1_4.copy(deep=True)
df_exercicio_1_5

#idx_maligno = df_exercicio_1_5[(df_exercicio_1_5['Densidade'] == '?') & (df_exercicio_1_5['Severidade'] == 'maligno')]['Densidade'].index
#df_exercicio_1_5[(df_exercicio_1_5['Densidade'] == '?') & (df_exercicio_1_5['Severidade'] == 'maligno')]['Densidade']

#idx_benigno = df_exercicio_1_5[(df_exercicio_1_5['Densidade'] == '?') & (df_exercicio_1_5['Severidade'] == 'benigno')]['Densidade'].index
#df_exercicio_1_5[(df_exercicio_1_5['Densidade'] == '?') & (df_exercicio_1_5['Severidade'] == 'benigno')]['Densidade']

def exercicio_1_5(df_exercicio_1_5):
    nome_classe_contorno = df_exercicio_1_5['Severidade'].unique()
    for nome_classe in nome_classe_contorno: 
        df_linha_ausente = df_exercicio_1_5[(df_exercicio_1_5['Densidade'] == '?') & (df_exercicio_1_5['Severidade'] == nome_classe)]
        if df_linha_ausente['Densidade'].count() > 0:
            df_contagem = df_exercicio_1_5[(df_exercicio_1_5['Densidade'] != '?') & (df_exercicio_1_5['Severidade'] == nome_classe)]
            frequencia_contorno_valor = df_contagem['Densidade'].value_counts().index.tolist()[0]
            #frequencia_forma_contagem = df_contagem['Forma'].value_counts()[0]
            df_exercicio_1_5.iloc[df_linha_ausente['Densidade'].index, [4]] = frequencia_contorno_valor 
            #= frequencia_forma_valor

exercicio_1_5(df_exercicio_1_5)

df_exercicio_1_5

#df_exercicio_1_5.iloc[idx_maligno, [4]]

#df_exercicio_1_5.iloc[idx_benigno, [4]]

"""# Exercício 2. Discretização - Método do encaixotamento de mesma largura"""

df_exercicio_2 = df_exercicio_1_5.copy(deep=True)

#Constroi as caixas com os valores em cada intervalo
def forma_bin(dados, inicio, boundary):
    if inicio < len(boundary):
        if boundary[inicio] != dados[len(dados)-1]: #intervalo [a, b)
            saida = list(filter(lambda x: (x >= boundary[inicio-1] and x < boundary[inicio]), dados))        
            return [saida] + forma_bin(dados, inicio+1, boundary)
        elif boundary[inicio] == dados[len(dados)-1]: # Se for o último elemento, o intervalo é fechado [a, b]            
            saida = list(filter(lambda x: (x >= boundary[inicio-1] and x <= boundary[inicio]), dados))
            return [saida]
    else:
        return []

def exercicio_2(df_exercicio_2):
    #Encaixotamento
    numBins = 6
    #array com as idades da base de dados
    dados = list(df_exercicio_2['Idade'].astype(int))
    #ordenação dos dados
    dados.sort()
    #print("Lista de dados:", dados)
    menor = min(dados)
    maior = max(dados)
    #print("menor:", menor, "\nmaior:", maior)
    intervalo = math.floor((maior - menor) / numBins)

    boundary = []
    for b in range(0,numBins+1):
        boundary = boundary + [(menor + b*intervalo)]
    #print("boundary:", boundary)
    

    #print("intervalo:", intervalo)
    bin = forma_bin(dados, 1, boundary)
    #print("Partição em caixas de mesma largura:", bin)
    #print("tamanho da Partição:", len(bin[0]))


    #Cálculo das médias de cada bin
    soma = 0
    media = []
    for lista in bin:
        for elemento in lista:
            soma = soma + elemento
        media = media + [math.floor(soma/len(lista))]
        soma = 0

    #print("Média de cada caixa:", media)

    #suavizacao: substituição dos valores de cada bin pela respectiva média
    bin_media = []
    for lista in bin:
        lista_temp = lista.copy()
        bin_media.append(lista_temp)

    for i in range(len(bin_media)):
        for j in range(len(bin_media[i])):
            bin_media[i][j] = media[i]

    #print("Suavização:", bin_media)

    #Substituição das idades pelas das médias obtidas no encaixotamento
    #Tornando os valores de idade em inteiros
    df_exercicio_2['Idade']  = df_exercicio_2['Idade'].astype(int)

    #Substituição
    for indice in range(len(media)): # São 5 bins, logo 6 médias no total
        for idade_caixa in np.unique(bin[indice]): 
            # Para cada valor de média, busca-se os valores únicos do bin associado
            df_exercicio_2['Idade'].replace({int(idade_caixa): media[indice]}, inplace=True)

#Chamada da função principal
exercicio_2(df_exercicio_2)

#for i in range(len(testeOriginal)):
#    print("Original:",testeOriginal[i], "Novo:", testeNovo[i])

#c = df_exercicio_2['Idade'].unique()
#c.sort()
#c

df_exercicio_2

df_exercicio_2['Idade'].unique()

"""# Exercício 3. Transformação dos dados - Normalização Max-Min"""

df_exercicio_3 = df_exercicio_1_5.copy(deep=True)
df_exercicio_3['Idade'] = df_exercicio_3['Idade'].astype(int)

def max_min(max , min, idade):
    novo_max = 1
    novo_min = 0
    valor_normalizado = ((idade - min) / (max - min)) * (novo_max - novo_min) + novo_min
    return valor_normalizado

def exercicio_3(df_exercicio_3):
    max_idade = max(df_exercicio_3['Idade'])
    min_idade = min(df_exercicio_3['Idade'])

    lista_idade_normalizada = []
    for idade in df_exercicio_3['Idade']:
        lista_idade_normalizada.append(max_min(max_idade, min_idade, idade))
    #Inserção de uma nova coluna no dataframe com a idade normalizada
    df_exercicio_3.insert(2, 'Idade_Normalizada', lista_idade_normalizada)    
exercicio_3(df_exercicio_3)

df_exercicio_3

"""# Exercício 4. Redução dos dados - Amostragem Estratificada"""

df_exercicio_4 = df_exercicio_1_5.copy(deep=True)

def exercicio_4(df_exercicio_4):
    tam_benigno = df_exercicio_4[df_exercicio_4['Severidade'] == 'benigno']['Severidade'].count()
    tam_maligno = df_exercicio_4[df_exercicio_4['Severidade'] == 'maligno']['Severidade'].count()
    tamanho_df = len(df_exercicio_4['Severidade'])

    #Proporção aproximada: maligno
    amostragem_maligno_tam_estratificada = (tam_maligno / tamanho_df)
    amostragem_maligno_tam_estratificada = int(round((amostragem_maligno_tam_estratificada * 100), 0))

    #Proporção aproximada: benigno
    amostragem_benigno_tam_estratificada = (tam_benigno / tamanho_df)
    amostragem_benigno_tam_estratificada = int(round((amostragem_benigno_tam_estratificada * 100), 0))

    frames_lista = []

    #Seleção aleatória: benigno
    df_amostragem_proporcional_benigno = df_exercicio_4[df_exercicio_4['Severidade'] == 'benigno']
    frames_lista.append(df_amostragem_proporcional_benigno.sample(n=amostragem_benigno_tam_estratificada))

    #Seleção aleatória: maligno
    df_amostragem_proporcional_maligno = df_exercicio_4[df_exercicio_4['Severidade'] == 'maligno']
    frames_lista.append(df_amostragem_proporcional_maligno.sample(n=amostragem_maligno_tam_estratificada))

    df_amostragem_estratificada_proporcional = pd.concat(frames_lista)
    df_amostragem_estratificada_proporcional.sort_index(inplace=True)

    return df_amostragem_estratificada_proporcional

df_amostragem_estratificada_proporcional = exercicio_4(df_exercicio_4)

df_amostragem_estratificada_proporcional[df_amostragem_estratificada_proporcional['Severidade'] == 'maligno']['Severidade'].count()

df_amostragem_estratificada_proporcional[df_amostragem_estratificada_proporcional['Severidade'] == 'benigno']['Severidade'].count()

df_amostragem_estratificada_proporcional