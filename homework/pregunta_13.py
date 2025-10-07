"""
Si la columna `c0` es la clave en los archivos `tbl0.tsv` y `tbl2.tsv`,
compute la suma de `tbl2.c5b` por cada valor en `tbl0.c1`.

Rta/
c1
A    146
B    134
C     81
D    112
E    275
Name: c5b, dtype: int64
"""

import pandas as pd
def pregunta_13():
    tbl0 = pd.read_csv('files/input/tbl0.tsv', sep='\t')
    tbl2 = pd.read_csv('files/input/tbl2.tsv', sep='\t') 

    tbl2['c5b'] = pd.to_numeric(tbl2['c5b'], errors='coerce').fillna(0).astype('int64')

    merged = pd.merge(
    tbl2,                    # detalle (tiene c5b)
    tbl0[['c0', 'c1']],      # dimensión (aporta c1)
    on='c0',
    how='inner'
    )

    resultado = (
    merged
    .groupby('c1')['c5b']
    .sum()
    .rename('c5b')           # nombre de la Serie
    # .sort_index()          # opcional: orden alfabético por c1
    )

    return resultado


print(pregunta_13())


