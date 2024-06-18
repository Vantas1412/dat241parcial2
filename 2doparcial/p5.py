import numpy as np
import scipy.sparse as sp
import multiprocessing as mp
from scipy.sparse import csr_matrix

def multiplicar_filas_particion(A, B, indices_filas):
    resultado_parcial = A[indices_filas, :] * B
    return resultado_parcial

def multiplicacion_paralela_matrices_sparse(A, B, num_procs):
    num_filas = A.shape[0]
    tamano_trozo = num_filas // num_procs
    pool = mp.Pool(processes=num_procs)

    resultados = []
    for i in range(num_procs):
        fila_inicial = i * tamano_trozo
        fila_final = fila_inicial + tamano_trozo if i < num_procs - 1 else num_filas
        indices_filas = range(fila_inicial, fila_final)
        resultados.append(pool.apply_async(multiplicar_filas_particion, args=(A, B, indices_filas)))

    pool.close()
    pool.join()

    resultado_combinado = sp.vstack([res.get() for res in resultados])
    return resultado_combinado

if __name__ == '__main__':
    
    tamano = 1000
    densidad = 0.01  
    A = sp.random(tamano, tamano, density=densidad, format='csr')
    B = sp.random(tamano, tamano, density=densidad, format='csr')

    num_procs = mp.cpu_count()  
    resultado_paralelo = multiplicacion_paralela_matrices_sparse(A, B, num_procs)

    print("Resultado de la multiplicación en paralelo:")
    print(resultado_paralelo.toarray())  


    resultado_secuencial = A.dot(B).toarray()

    print("\nComparación con el resultado secuencial:")
    print(np.allclose(resultado_paralelo.toarray(), resultado_secuencial))
