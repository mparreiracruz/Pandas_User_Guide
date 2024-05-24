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

print(df2.dtypes)
