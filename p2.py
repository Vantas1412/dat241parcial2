nodos = [0, 1, 2, 3, 4]
bordes = [
    (0, 1),
    (0, 2),
    (1, 2),
    (1, 3),
    (2, 3),
    (3, 4)
]


n = len(nodos)
matriz_dispersa = [[0 for _ in range(n)] for _ in range(n)]

for (i, j) in bordes:
    matriz_dispersa[i][j] = 1
    matriz_dispersa[j][i] = 1  

# Imprimir la matriz dispersa
for fila in matriz_dispersa:
    print(fila)
