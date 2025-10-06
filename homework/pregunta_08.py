"""
Agregue una columna llamada `suma` con la suma de `c0` y `c2` al
data frame que contiene el archivo `tbl0.tsv`.

Rta/
     c0  c1   c2          c3  suma
0     0   E    1  1999-02-28     1
1     1   A    2  1999-10-28     3
2     2   B    5  1998-05-02     7
...
37   37   C    9  1997-07-22    46
38   38   E    1  1999-09-28    39
39   39   E    5  1998-01-26    44

"""
import pandas as pd
def pregunta_08():

     table0 = pd.read_csv('files/input/tbl0.tsv', sep='\t')

     table0['suma'] = table0['c0'] + table0['c2']

     return table0
     

print(pregunta_08())