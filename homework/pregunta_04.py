"""
Calcule el promedio de `c2` por cada letra de la `c1` del archivo
`tbl0.tsv`.

Rta/
c1
A    4.625000
B    5.142857
C    5.400000
D    3.833333
E    4.785714
Name: c2, dtype: float64
"""

import pandas as pd

def pregunta_04():
    table0 = pd.read_csv('files/input/tbl0.tsv', sep='\t')

    return table0.groupby('c1')['c2'].agg('mean')

print(pregunta_04())


