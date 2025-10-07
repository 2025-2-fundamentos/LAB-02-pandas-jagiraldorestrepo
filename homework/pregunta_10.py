"""
Construya una tabla que contenga `c1` y una lista separada por ':' de los
valores de la columna `c2` para el archivo `tbl0.tsv`.

Rta/
                                c2
c1
A               1:1:2:3:6:7:8:9
B                 1:3:4:5:6:8:9
C                     0:5:6:7:9
D                   1:2:3:5:5:7
E   1:1:2:3:3:4:5:5:5:6:7:8:8:9
"""
import pandas as pd



def pregunta_10():
    table0 = pd.read_csv('files/input/tbl0.tsv', sep='\t')

    grouped = (table0
               .groupby('c1')['c2']
               .apply(lambda x: ':'.join(str(i) for i in sorted(x)))
               .to_frame(name='c2'))

    return grouped


# import pandas as pd

# # 1️⃣ defines la función fuera
# def unir_y_ordenar(valores):
#     """
#     Recibe una Serie (columna c2 de cada grupo)
#     y devuelve los valores ordenados y unidos con ':'
#     """
#     return ':'.join(str(i) for i in sorted(valores))

# # 2️⃣ usas la función dentro del apply
# def pregunta_10_alternativa():
#     table0 = pd.read_csv('files/input/tbl0.tsv', sep='\t')

#     result = (
#         table0.groupby('c1')['c2']
#         .apply(unir_y_ordenar)        # 👈 aquí va la función
#         .to_frame(name='c2')
#     )

#     return result



print(pregunta_10())