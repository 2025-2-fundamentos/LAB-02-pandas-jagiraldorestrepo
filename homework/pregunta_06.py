

"""
Retorne una lista con los valores unicos de la columna `c4` del archivo
`tbl1.csv` en mayusculas y ordenados alfabéticamente.

Rta/
['A', 'B', 'C', 'D', 'E', 'F', 'G']

"""

import pandas as pd
def pregunta_06():
    table1 = pd.read_csv('files/input/tbl1.tsv', sep='\t')

    lista_unicos = table1['c4'].unique() #devuelve un array de numpy, no un str, por eso lo tengo que convertir a list
    

    #aqui yo haría tolist().sort() pero eso devuelve none
    #porque lo unico que hace es ordenarla en el instante
    lista_unicos = lista_unicos.tolist()

    #aqui ya habia retornado con sorted(lista_unicos).upper(), pero esto
    #es un metodo para strings, asi que hago la list comprehension

    lista_unicos = [x.upper() for x in lista_unicos]

    return sorted(lista_unicos)


print(pregunta_06())