"""
¿Cuál es la cantidad de registros por cada letra de la columna `c1` del
archivo `tbl0.tsv`?

Rta/
c1
A     8
B     7
C     5
D     6
E    14
Name: count, dtype: int64

c0	c1	c2	c3
0	E	1	1999-02-28
1	A	2	1999-10-28
"""
import pandas as pd
def pregunta_03():
    table0 = pd.read_csv('files/input/tbl0.tsv', sep='\t')
    
    return table0.value_counts('c1').sort_index()




