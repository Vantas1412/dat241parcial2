import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse import random
filas = 1000
columnas = 1000
densidad = 0.01  


matriz1 = random(filas, columnas, density=densidad, format='csr', data_rvs=lambda size: np.random.randint(1, 101, size))
matriz2 = random(columnas, filas, density=densidad, format='csr', data_rvs=lambda size: np.random.randint(1, 101, size))

resultado = matriz1.dot(matriz2)


print(f"Matriz 1: \n{matriz1}")
print(f"Matriz 2: \n{matriz2}")
print(f"Resultado de la multiplicación: \n{resultado}")
