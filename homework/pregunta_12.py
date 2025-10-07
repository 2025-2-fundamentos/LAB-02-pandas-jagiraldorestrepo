"""
Construya una tabla que contenga `c0` y una lista separada por ','
de los valores de la columna `c5a`  y `c5b` (unidos por ':') de la
tabla `tbl2.tsv`.

Rta/
     c0                                   c5
0     0        bbb:0,ddd:9,ggg:8,hhh:2,jjj:3
1     1              aaa:3,ccc:2,ddd:0,hhh:9
2     2              ccc:6,ddd:2,ggg:5,jjj:1
...
37   37                    eee:0,fff:2,hhh:6
38   38                    eee:0,fff:9,iii:2
39   39                    ggg:3,hhh:8,jjj:5
"""

import pandas as pd

def pregunta_12():
     import pandas as pd
     table0 = pd.read_csv('files/input/tbl2.tsv', sep='\t')

     result = (
          table0
          .assign(c5 = table0['c5a'].astype(str) + ':' + table0['c5b'].astype(str))  # combina columnas
          .groupby('c0')['c5']
          .apply(lambda x: ','.join(sorted(x)))  # une por grupo
          .to_frame(name='c5')
          .reset_index()
     )

     return result

print(pregunta_12())
