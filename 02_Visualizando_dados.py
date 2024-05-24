import pandas as pd
import numpy as np

'''
Criação de objeto 
Consulte a seção Introdução às estruturas de dados.

Criando um Series passando uma lista de valores, permitindo que os pandas
criem um arquivo RangeIndex.
'''

s = pd.Series([1, 3, 5, np.nan, 6, 8])
#print(s)

'''
Criando um DataFrame passando um array NumPy com um índice de data e hora 
usando date_range() colunas rotuladas:
'''

dates = pd.date_range("20130101", periods=6)
#print(dates)

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
#print(df)

'''
Criando um DataFramepassando um dicionário de objetos onde as chaves são os
rótulos das colunas e os valores são os valores das colunas.
'''

df2 = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": np.array([3] * 4, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo",
    }
)
#print(df2)

'''
As colunas do resultado DataFrametêm dtypes diferentes :
'''

#print(df2.dtypes)

#-----------------------------------02_Visualizando_dados-----------------------------------

'''
Use DataFrame.head()e DataFrame.tail()para visualizar as linhas 
superior e inferior do quadro, respectivamente:
'''

# print(df.head())
# print(df.tail(3))

'''
Exibir o DataFrame. index ou DataFrame.columns:
'''

# print(df.index)
# print(df.columns)

'''
Retorne uma representação NumPy dos dados subjacentes 
DataFrame.to_numpy() sem os rótulos de índice ou coluna:
'''

#print(df.to_numpy())

#print(df2.dtypes)

#print(df2.to_numpy())

#print(df.describe())  # mostra um rápido resumo estatístico de seus dados

#print(df.T)  # Transpondo seus dados

#print(df.sort_index(axis=1, ascending=False))  # classifica por um eixo

print(df.sort_values(by="B"))  # classifica por valores
