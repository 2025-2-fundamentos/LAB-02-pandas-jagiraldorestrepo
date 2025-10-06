"""
Agregue el año como una columna al dataframe que contiene el archivo
`tbl0.tsv`.

Rta/
    c0 c1  c2          c3  year
0    0  E   1  1999-02-28  1999
1    1  A   2  1999-10-28  1999
2    2  B   5  1998-05-02  1998
...
36  36  B   8  1997-05-21  1997
37  37  C   9  1997-07-22  1997
38  38  E   1  1999-09-28  1999
39  39  E   5  1998-01-26  1998

"""
import pandas as pd
def pregunta_09():
    table0 = pd.read_csv('files/input/tbl0.tsv', sep='\t')

    table0['year'] = table0['c3'].str.split('-').str[0]

    return table0

print(pregunta_09())